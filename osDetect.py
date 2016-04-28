#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Script to detect the operting system. Will look for the location of the python binary and return the OS type.
print("Detecting operating system...")

import os

def osType():
	winPyPath = 'C:\Program Files (x86)\Python2.7'
	linPyPath = '/usr/lib/python2.7'

	winPyPathExists = os.path.exists(winPyPath)
	linPyPathExists = os.path.exists(linPyPath)
	
	if winPyPathExists == True:
		print("Currently running on Windows")
	elif winPyPathExists == False & linPyPathExists == True:
		print("Currently running on Linux")
	else: 
		print("Error: OS not supported")	

osType()

