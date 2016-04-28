#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Script to dump the contents of a registry hive to a user-specified file

import os, sys
from _winreg import *
from sys import argv

scriptName, outputFile = argv

def versionCheck():
	if sys.version_info<(2,7,0):
		sys.stderr.write("Python 2.7 or later required for this script\n")
		exit(1)

versionCheck()

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

of1 = open(outputFile, "w")

for i in range(QueryInfoKey(aKey)[1]):
	try:
		n,v,t = EnumValue(aKey,i)
		print(n, v, t)
	except EnvironmentError:
		print("You have",i," tasks starting at logon...")
		break

CloseKey(aKey)
CloseKey(aReg)

of1.close()	

	
