#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

from __future__ import absolute_import

import os
import subprocess
import sys
import tempfile

from codecs import open

CUSTOM_COMPILE_COMMAND = 'tox -e flap'
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REQUIREMENTS_FILENAME = 'requirements.txt'
VENV_PATH = os.path.join(ROOT_PATH, '.venv/bin/')


def _cleanup(file_ref):
    def _strip(line):
        return line.strip()
    return filter(None, map(_strip, file_ref))


def _group_requirements(files):
    collected = set()
    for file in files:
        with open(file, encoding='utf-8') as f:
            collected.update(_cleanup(f))
    return sorted(collected)


def collect_requirements():
    requirement_files = []
    for top_level in os.listdir(ROOT_PATH):
        top_level_path = os.path.join(ROOT_PATH, top_level)
        if not os.path.isdir(top_level_path):
            continue
        requirements_path = os.path.join(top_level_path, REQUIREMENTS_FILENAME)

        if os.path.exists(requirements_path):
            requirement_files.append(requirements_path)

    return _group_requirements(sorted(requirement_files))


def write_to_root_requirements(reqs):
    custom_env = os.environ.copy()
    custom_env['PATH'] = custom_env['PATH'] + ':' + VENV_PATH
    custom_env['CUSTOM_COMPILE_COMMAND'] = CUSTOM_COMPILE_COMMAND

    with tempfile.NamedTemporaryFile() as inp:
        inp.write('\n'.join(reqs).encode('utf-8'))
        inp.flush()

        subprocess.check_call(
            ['pip-compile',
             '--annotate',
             '--verbose',
             '--output-file',
             os.path.join(ROOT_PATH, REQUIREMENTS_FILENAME),
             inp.name],
            env=custom_env,
        )


if __name__ == "__main__":
    requirements = collect_requirements()
    write_to_root_requirements(requirements)
