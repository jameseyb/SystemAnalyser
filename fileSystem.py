#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Script to dump the contents of a registry hive to a user-specified file

import os, sys, re

#Check the version of Python with this function, ensures things actually work.
def versionCheck():
	if sys.version_info<(2,7,0):
		sys.stderr.write("Python 2.7 or later required for this script\n")
		exit(1)
	else:
		sys.stdout.write("Version check passed. Continuing...\n\n")

#Check Python version and display error if requirements are not met		
versionCheck()

#Script main body here

searchString = input("Enter string to search for: ")

try:
	for root, dirs, files in os.walk("\\", topdown=True):
		for name in dirs:
			searchObj = re.search(searchString, name, re.M|re.I)
		if searchObj:
			print(os.path.join(root, name))
		for name in files:
			searchObj = re.search(searchString, name, re.M|re.I)
		if searchObj:
			print(os.path.join(root, name))

except WindowsError as e:
	print(e)