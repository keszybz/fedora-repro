#!/usr/bin/python
# SPDX-License-Identifier: LGPL-2.1-or-later

import sys

from fedora_repro import worker

if __name__ == '__main__':
    worker.main(sys.argv[1:])
