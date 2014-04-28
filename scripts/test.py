#!/usr/bin/env python
"""Runs all unit tests."""

import os
import subprocess

# To support running this file from the root, pylint: disable=F0401
import common
# pylint: enable=F0401


def run_tests():
    """Runs unit tests using nose and the NoseGAE plugin."""
    app_engine_dir = common.get_app_engine_dir()
    project_dir = common.get_project_dir()
    # NoseGAE wants us to be in the project directory.
    os.chdir(project_dir)
    # TODO(samking): Use https://github.com/jkrebs/nose-gae-index to
    # automatically update indexes when unit tests are run.
    subprocess.call(
        ['nosetests', '--with-gae', '--without-sandbox', '--gae-lib-root',
         app_engine_dir, '--nologcapture', project_dir])


if __name__ == '__main__':
    run_tests()
