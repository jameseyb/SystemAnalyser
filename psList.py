#!/usr/bin/python

#Import required libraries
import sys, os, subprocess, psutil, pprint
from sys import argv
#from subprocess import call

scriptName, outFile = argv
print "Usage = $ python psList.py <output filename>\n"

#Open output file
#fo1 = open(outFile, "w")

#Initial formatting
#XML/JSON formatting

#list running process and write to file
#pl1 = subprocess.Popen(['ps', '-aux'], stdout=subprocess.PIPE).communicate()[0]
#fo1.write("<Process Information>\n")
#fo1.write(pl1)
#fo1.write("\n")
#print "Process information written to file..."

#list running processes using psutil
#fo1.write("<Process Information>\n")
for proc in psutil.process_iter():
  try:
    pinfo = proc.as_dict(attrs = ['pid', 'name'])
    pfiles = proc.as_dict(attrs = ['open_files'])
  except psutil.NoSuchProcess:
    pass
  else:
    print(pinfo, pfiles)
  

#fo1.write(pla)
#fo1.write("\n")


#list open ports and write to file
#pl2 = subprocess.Popen(['sudo', 'netstat', '-anp'], stdout=subprocess.PIPE).communicate()[0]
#fo1.write("<Port Information>\n")
#fo1.write(pl2)
#fo1.write("\n")
#print "port information written to file...\n"

#Close output file
#fo1.close()
#print "Output file closed"

