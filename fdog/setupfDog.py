# -*- coding: utf-8 -*-

#######################################################################
# Copyright (C) 2020 Vinh Tran
#
#  This script is used to setup fdog: install dependencies and
#  download pre-computed data
#
#  This script is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License <http://www.gnu.org/licenses/> for
#  more details
#
#  Contact: tran@bio.uni-frankfurt.de
#
#######################################################################

import sys
import os
import argparse
import subprocess
from pathlib import Path

def checkOptConflict(lib, conda):
    if lib:
        if (conda):
            sys.exit('*** ERROR: --lib and --conda cannot be used at the same time!')

def main():
    version = '0.0.1'
    parser = argparse.ArgumentParser(description='You are running fdog.setup version ' + str(version) + '.')
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument('-o', '--outPath', help='Output path for fdog data', action='store', default='', required=True)
    optional.add_argument('--conda', help='Setup fdog within a conda env', action='store_true', default=False)
    optional.add_argument('--lib', help='Install fdog libraries only', action='store_true', default=False)
    optional.add_argument('--getPath', help='Get path to installed fdog', action='store_true', default=False)

    ### get arguments
    args = parser.parse_args()
    conda = args.conda
    lib = args.lib
    checkOptConflict(lib, conda)
    outPath = args.outPath
    Path(outPath).mkdir(parents = True, exist_ok = True)
    fdogPath = os.path.realpath(__file__).replace('/setupfDog.py','')
    ### get path
    if args.getPath:
        print(fdogPath)
        sys.exit()
    ### run setup
    if conda:
        setupFile = '%s/setup/setup_conda.sh -o %s' % (fdogPath, outPath)
        subprocess.call([setupFile], shell = True)
    else:
        if lib:
            setupFile = '%s/setup/setup.sh -l' % (fdogPath)
        else:
            setupFile = '%s/setup/setup.sh -o %s' % (fdogPath, outPath)
        subprocess.call([setupFile], shell = True)

if __name__ == '__main__':
    main()
