#!/usr/bin/python

'''
@package display
@author Brahayam Ponton (brahayam.ponton@tuebingen.mpg.de)
@license License BSD-3-Clause
@copyright Copyright (c) 2019, New York University and Max Planck Gesellschaft.
@date 2019-10-07

Use example: ipython ../../../scripts/display.py -- -i ./cfg_demo01_lqr_results.yaml
'''

import sys, getopt
from helpers import Graphics

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'display.py -i <datafile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'display.py -i <datafile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    motion = Graphics()
    motion.show_motion(inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
