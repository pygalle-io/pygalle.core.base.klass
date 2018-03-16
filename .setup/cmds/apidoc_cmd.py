import distutils.log



class BuildApiCommand(distutils.cmd.Command):
    """A custom command to build api document with Sphinx"""

    description = 'run sphinx-apidoc'
    user_options = []

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.

    def finalize_options(self):
        """Post-process options."""

    def run(self):
        from sphinx.apidoc import main
        """Run command."""
        try:
            from sphinx.ext.apidoc import main as sphinx_apidoc
            sphinx_apidoc(['-f', '-o', './docs', './src/pygalle'])
            #self.run_command('build_sphinx')
        except:
            pass
