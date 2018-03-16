import distutils
import os

from settings import SETTINGS

README = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'README.md')

from jinja2 import Environment, FileSystemLoader

class GenerateReadmeCommand(distutils.cmd.Command):

    description = 'generate README.md from templates and settings'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print('Generating README')
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', '..', '.templates')))
        template = env.get_template('README.md.jinja')
        output_from_parsed_template = template.render(SETTINGS)
        f = open(README, 'w')
        f.write(output_from_parsed_template)
        f.close()
