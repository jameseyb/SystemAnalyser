#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function

#Script to recursively search the registry for a user specified string

import os
import sys
import winreg
from sys import argv

script, inputname = argv

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
		except OSError as e:
			return None
			
def printValues(hkey): #Returns values in regitry keys
	for i in range(winreg.QueryInfoKey(hkey)[1]):
		n,v,t = winreg.EnumValue(hkey,i)
		of1.write('\t' + str(n) + ',' + str(v) +',' + str(t) + '\n')
	
def traverse_registry_tree(hkey, keypath): #Function walks down the hive and writes the registry keys to a file.
	try:
		key = winreg.OpenKey(hkey, keypath, 0, winreg.KEY_READ)
		printValues(key)
		for subkeyname in subkeys(key):
			of1.write(keypath + '\\' + subkeyname + '\n')
			try:
				subkeypath = "%s\\%s" % (keypath, subkeyname)
				traverse_registry_tree(hkey, subkeypath)
			except:
				raise
	except WindowsError as e:
		raise
	finally:
		winreg.CloseKey(key)

#Pre-script checks
versionCheck()		
		
#Script main body here
if __name__ == '__main__':

	#Connect to registry and correct location
	keypath = str("Software" + "\\" + inputname)
	print("Path found: " + keypath)
	
	#Walk first registry entry
	of1 = open(inputname + "_HKCU" + ".log", "w")
	try:
		traverse_registry_tree(winreg.HKEY_CURRENT_USER, keypath)
	finally:
		of1.close()
