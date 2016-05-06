#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function

#Script to recursively search the registry for a user specified string

import os
import sys
import winreg

#Functions here
def versionCheck(): # Checks the version of python installed
	if sys.version_info<(2,7,0):
		sys.stderr.write("Python 2.7 or later required for this script\n")
		exit(1)
	else:
		sys.stdout.write("Version check passed. Continuing...\n\n")

def subkeys(key): #Function iterates over the keys in the current registry folder and returns the subkeys
	i = 0
	while True:
		try:
			subkey = winreg.EnumKey(key, i)
			yield subkey
			i+=1
		except WindowsError as e:
			break		

def traverse_registry_tree(hkey, keypath): #Function walks down the hive and writes the registry keys to a file.
	try:
		key = winreg.OpenKey(hkey, keypath, 0, winreg.KEY_READ)
		for subkeyname in subkeys(key):
			of1.write(keypath + '\\' + subkeyname + '\n')
			for i in range(winreg.QueryInfoKey(key)[1]):
				n,v,t = winreg.EnumValue(key,i)
				of1.write('\t' + str(n) + ',' + str(v) +',' + str(t) + '\n')
			subkeypath = "%s\\%s" % (keypath, subkeyname)
			traverse_registry_tree(hkey, subkeypath)
	except WindowsError as e:
		print("Specified path in registry (" + keypath + ") does not exist\n")

#Pre-script checks
versionCheck()		
		
#Script main body here
if __name__ == '__main__':

	#Connect to registry and correct location
	inputname = str(input("Enter string to search for: "))
	keypath = str(r"Software" + "\\" + inputname)
	print("Path found: " + keypath)
	
	#Walk first registry entry
	of1 = open(inputname + "_HKCU" + ".log", "w")
	traverse_registry_tree(winreg.HKEY_CURRENT_USER, keypath)
	of1.close()
