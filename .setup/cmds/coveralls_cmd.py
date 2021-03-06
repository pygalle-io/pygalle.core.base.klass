

import distutils


class CoverallsCommand(distutils.cmd.Command):
    description = 'generate README.md from templates and settings'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            from coveralls.cli import main as coveralls_cli
            print('Run coveralls')
            coveralls_cli([])
        except:
            pass
