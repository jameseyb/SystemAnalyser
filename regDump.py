#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Script to dump the contents of a registry hive to a user-specified file

import os, sys, winreg
from sys import argv

scriptName, outputFile = argv

#Custom functions here

def versionCheck():
	if sys.version_info<(2,7,0):
		sys.stderr.write("Python 2.7 or later required for this script\n")
		exit(1)
	else:
		sys.stdout.write("Version check passed. Continuing...\n\n")

#Script main body here

#Check Python version and display error if requirements are not met		
versionCheck()

#Connect to registry and correct location
keypath = r"Software\Citrix"

#Open logfile
of1 = open(outputFile, "w")

def subkeys(key):
    i = 0
    while True:
        try:
            subkey = winreg.EnumKey(key, i)
            yield subkey
            i+=1
        except WindowsError as e:
            break

def traverse_registry_tree(hkey, keypath, commas=0):
    key = winreg.OpenKey(hkey, keypath, 0, winreg.KEY_READ)
    for subkeyname in subkeys(key):
        for i in range(winreg.QueryInfoKey(key)[1]):
            n,v,t = winreg.EnumValue(key,i)
            of1.write(','*commas + subkeyname + ',' + str(n) + ',' + str(v) +',' + str(t) + '\n')
        subkeypath = "%s\\%s" % (keypath, subkeyname)
        traverse_registry_tree(hkey, subkeypath, commas+1)

traverse_registry_tree(winreg.HKEY_CURRENT_USER, keypath)

of1.close()	

	

