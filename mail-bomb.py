#!/usr/bin/python3

# Author: spredditt

import sys, os

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def helpmenu():
    try:
        doc = open('documentation.txt', 'r')
        print(' ')
        print(doc.read())
        doc.close()
    except IOError:
        print('Banner File not found')

if sys.argv[1] in ('-a', '-t', '-m', '-h', '--host-mail', '--target', '--mail-type', '--help'):
    print('Pass')
else:
    helpmenu()