#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Script to detect the operting system. Will look for the location of the python binary and return the OS type.
print("Detecting operating system...")

import os
#from sys import argv

winPyPath = 'C:\Program Files (x86)\Python2.7'
linPyPath = '/usr/lib/python2.7'

print(winPyPath)
print(linPyPath)

pyPathExists = os.path.exists(winPyPath)
print(pyPathExists)
	

pyPathIsDir = os.path.isdir('C:\Program Files (x86)\Python2.7')
print(pyPathIsDir)

