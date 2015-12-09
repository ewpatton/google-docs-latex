#!/bin/bash
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

# Configure the project name and directory
PROJECT_DIR=${PROJECT_DIR:-changeme}
PROJECT=${PROJECT:-changeme}

# Configure TeX engines
TEX=${TEX:-xelatex}
BIBTEX=${BIBTEX:-bibtex}

set -e
export PATH="$PATH:~/bin:/usr/local/bin"
OS=`uname`
case ${OS} in
    Darwin)
        PATH="$PATH:/Library/TeX/texbin"
        ;;

    Linux)
        PATH="$PATH:/usr/texbin"
        ;;
esac
source ~/.gdrive_env/bin/activate

python -m gdrive_latex.main "$PROJECT.tex" "$PROJECT.bib"
if [[ -e "$PROJECT.tex" ]] && [[ -e "$PROJECT.bib" ]]; then
    ${TEX} "${PROJECT}.tex"
    ${BIBTEX} "${PROJECT}.aux"
    ${TEX} "${PROJECT}.tex"
    ${TEX} "${PROJECT}.tex"
fi

rm -f ${PROJECT}.{tex,bib,blg,bbl,aux,out}
