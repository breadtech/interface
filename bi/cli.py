#!/usr/bin/env python

from sys import argv
from argparse import menu

# check number of args at least needs a cmd
n = len(argv)

if n == 1:
  print menu['help']['help']
  exit()
else:
  try:
    print menu[argv[1]][argv[2]]
  except:
    print 'bi: ' + cmd + ': commmand not found'
