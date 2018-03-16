

import distutils
import os

from settings import SETTINGS

README = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'README.md')

class CoverageCommand(distutils.cmd.Command):

    description = 'generate README.md from templates and settings'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print('Run coverage')
        try:
            from coverage.cmdline import main as coverage_cli
            coverage_cli(['run', '--source=src/pygalle', 'setup.py', 'test'])
        except:
            pass
