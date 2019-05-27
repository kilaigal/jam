#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

from __future__ import absolute_import

import sys
import subprocess as sp


def install_pkg(pkg_name):
    process = sp.Popen(
        [sys.executable, 'setup.py', 'develop', '-N'],
        stdout=sp.PIPE,
        cwd=pkg_name
    )
    output, unused_err = process.communicate()
    ret_code = process.wait()
    if 0 != ret_code:
        raise sp.CalledProcessError(ret_code, CMD[0], output=output)


if __name__ == '__main__':
    for this_pkg in {'arches'}:
        install_pkg(this_pkg)
