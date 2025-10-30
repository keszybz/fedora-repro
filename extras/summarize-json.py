#!/usr/bin/python
# SPDX-License-Identifier: LGPL-2.1-or-later

import json
import re
import sys
from pathlib import Path

# Format specification: https://rb.zq1.de/spec/json-format.txt

def read_input(filename):
    f = filename.open('r')
    data = json.load(f)

    for k in data.keys():
        if k.endswith('.src'):
            m = re.match(r'^(.*)-([^-]+)-([^-]+)$', k[:-4])
            name, version, revision = m.groups()
            break
    else:
        raise 'src not found'

    # We report 'unreproducible' if any of the binary rpms differ,
    # otherwise 'reproducible'. The srpm is excluded.
    have_mods = any(v for k,v in data.items()
                    if not k.endswith('.src'))

    return {
        'architecture' : 'x86_64',
        # 'build_date' : 1486187303,
        'package' : name,
        'status' : ('unreproducible' if have_mods else 'reproducible'),
        'release' : 'Fedora:rawhide',
        'version' : version,
    }

if __name__ == '__main__':
    args = sys.argv[1:]

    arr = []
    for filename in sorted(args):
        p = Path(filename)
        data = read_input(p)
        arr += [data]

    print(json.dumps(arr, indent=2))
