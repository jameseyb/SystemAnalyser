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

#inputName = input("Enter name of folder to search for: ")

searchPath = "C:\\Drop_Zone\\Projects\\SystemAnalyser"

try:
	for path, dirs, files in os.walk(searchPath, topdown=True):
		for files in os.walk(path, topdown=True):
			str(searchRes) = re.search(r'citrix', files, re.M|re.I)
			if searchRes:
				print(searchRes)
			else:
				print("No matches found")
except WindowsError as e:
	print("Error")