#!/usr/bin/python3

# Author: spredditt

import sys, os, getpass

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def helpmenu(message):
    print(message)
    try:
        doc = open('documentation.txt', 'r')
        print(' ')
        print(doc.read())
        doc.close()
    except IOError:
        print('Banner File not found')

hostmail = ''
hostpass = ''
targetmail = ''
mailtype = ''

validSyntax = True

try:
    if sys.argv[1] in ('-h', '--help'):
        helpmenu('')

    else:
        for i in range(1, 6, 2):
            if sys.argv[i] not in ('-a', '-t', '-m', '--host-mail', '--target-mail', '--mail-type'):
                helpmenu('\nInvalid syntax')
                SystemExit
            else:
            
                if sys.argv[i + 1] == '' or sys.argv[i + 1] in ('-a', '-t', '-m', '--host-mail', '--target-mail', '--mail-type'):
                    helpmenu(f'\nInvalid value at {sys.argv[i]}')
                    break
                else:
                    hostpass = getpass.getpass('host-password: ')
                    SystemExit
except IndexError:
    helpmenu('')