#!/usr/bin/python
# SPDX-License-Identifier: LGPL-2.1-or-later

# https://kojipkgs.fedoraproject.org//packages/systemd/254/1.fc39/data/logs/x86_64/root.log
# pylint: disable=missing-docstring,invalid-name,consider-using-with,unspecified-encoding

import argparse
import sys

from fedora_repro import builder

def do_opts(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--koji-profile', default='koji')
    parser.add_argument('--mock-uniqueext', default='repro',
                        help="Mock build identifier, e.g. 'builder1' or '{p.canonical}'")
    parser.add_argument('--debug',
                        action='store_true')
    parser.add_argument('--debug-xmlrpc',
                        action='store_true')
    parser.add_argument('-d', '--diff',
                        action='store_true')

    parser.add_argument('rpm')

    opts = parser.parse_args(argv)
    return opts

def main(argv):
    opts = do_opts(argv)
    rpm = builder.RPM.from_string(opts.rpm, is_package=True)

    # TODO: stop passing opts into builder functions
    builder.init_koji_session(opts)

    if opts.diff:
        return builder.compare_package(opts, rpm)

    sys.exit(builder.rebuild_package(opts, rpm))

if __name__ == '__main__':
    main(sys.argv[1:])
