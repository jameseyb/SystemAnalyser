#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function

#Script to recursively search the filesystem for a user specified string.

import os
import sys 
import re 
import datetime

#Functions here
def versionCheck(): #Checks the version of python installed
	if sys.version_info<(2,7,0):
		sys.stderr.write("Python 2.7 or later required for this script\n")
		exit(1)
	else:
		sys.stdout.write("Version check passed. Continuing...\n\n")

def recursiveCheck(): #recursively search filesystem for the search string
	try:
		for root, dirs, files in os.walk("\\", topdown=True):
			for name in dirs:
				searchObj = re.search(searchString, name, re.M|re.I)
			if searchObj:
				print("Match found")
				of1.write(os.path.join(root, name) + '\n')
			for name in files:
				searchObj = re.search(searchString, name, re.M|re.I)
			if searchObj:
				print("Match found")
				of1.write(os.path.join(root, name) + '\n')
	except WindowsError as e:
		print(e)

#Pre-script checks
versionCheck()

#Script main body here
if __name__ == '__main__':

	searchString = str(input("Enter string to search for: "))
	ds = str(datetime.date.today())

	of1 = open(ds + '-' + searchString + ".log", "w")
	recursiveCheck()
	of1.close()
