#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
---
This file is part of pygalle.core.base.klass
Copyright (c) 2018 SAS 9 Février.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---
"""

import os
import yaml
from pygit2 import Repository

configuration_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'settings.yml')

travis_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '.travis.yml')

SETTINGS = yaml.load(open(configuration_filename, 'r'))
SETTINGS['pythons'] = yaml.load(open(travis_filename, 'r'))['python']
try:
    SETTINGS['github']['branch'] = Repository('.').head.shorthand
except:
    SETTINGS['github']['branch'] = 'master'

README = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')
