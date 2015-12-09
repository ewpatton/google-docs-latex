# -*- coding: utf-8 -*-
#
# This package is part of the gdrive_latex package.
# Copyright © 2015 Evan W. Patton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(
    name='google-docs-latex',
    version='0.1',
    packages=['gdrive_latex'],
    url='https://github.com/ewpatton/google-docs-latex',
    license='GPLv3+',
    author='Evan W. Patton',
    author_email='ewpatton@gmail.com',
    description='A small helper tool for compiling collaboratively edited LaTeX in Google Docs.'
)
