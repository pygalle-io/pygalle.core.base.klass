from distutils.command.build import build


class Build(build):
    sub_commands = [('test', None),
                    ('lint', None),
                    ('readme', None),
                    ('apidoc', None),
                    ('coverage', None),
                    ('coveralls', None)
                    ] + build.sub_commands