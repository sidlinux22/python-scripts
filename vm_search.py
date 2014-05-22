#!/usr/bin/python2.7
import re
import sys
import os
import csv
import subprocess

#~sid

if len(sys.argv) <  2:
    print "Argument required", sys.argv[1:]
    sys.exit()




os.environ[" OS_PASSWORD"] = "XYZ" #Provide your passwd hash
os.environ["OS_REGION_NAME"] = ""
os.environ["OS_TENANT_NAME"] = ""
os.environ["OS_USERNAME"] = ""                    #Provide your username
os.environ[" OS_AUTH_STRATEGY"] = "keystone"


def dal_one():
    if re.match( r'^102.60.16[0,1,4,5]', ipaddress, re.M|re.I):
       print " Cloud One  Region #1"
       os.environ["OS_AUTH_URL"] = "http:cloudone-001-api-endpoint.example.com:6000/v2.0/"
    else:
       print " Cloud One Region #2"
       os.environ["OS_AUTH_URL"] = "http:cloudone-002-api-endpoint.example.com:6000/v2.0/"
    cat = subprocess.Popen(['nova', 'list'], 
                           stdout=subprocess.PIPE,
                        )
    grep = subprocess.Popen(['grep','-w', sys.argv[1]],
                           stdin=cat.stdout,
                           stdout=subprocess.PIPE,
                        )
    end_of_pipe = grep.stdout
    for line in end_of_pipe:
        print line


def dal_two():
    if re.match( r'^101.60.([1,0,7][^10,^14,^8]).*', ipaddress, re.M|re.I):
        print " Cloud One Region #3"
        os.environ["OS_AUTH_URL"] = "http:cloudone-003-api-endpoint.example.com:6000/v2.0/"
    else:
        print " Cloud One  Region #4"
        os.environ["OS_AUTH_URL"] = "http:cloudone-004-api-endpoint.example.com:6000/v2.0/"
    cat = subprocess.Popen(['nova', 'list'],
                           stdout=subprocess.PIPE,
                        )
    grep = subprocess.Popen(['grep','-w', sys.argv[1]],
                           stdin=cat.stdout,
                           stdout=subprocess.PIPE,
                        )
    end_of_pipe = grep.stdout
    for line in end_of_pipe:
        print line


def dfw_one():
    if re.match( r'^192.62.3[^8,^4,^5].*', ipaddress, re.M|re.I):
       print "Cloud  Region #1"
       os.environ["OS_AUTH_URL"] = "http:cloudtwo-001-api-endpoint.example.com:6000/v2.0/"
    else:
       print "Cloud Two  Region #2"
       os.environ["OS_AUTH_URL"] = "http:cloudtwo-002-api-endpoint.example.com:6000/v2.0/"
    cat = subprocess.Popen(['nova', 'list'],
                           stdout=subprocess.PIPE,
                        )
    grep = subprocess.Popen(['grep','-w', sys.argv[1]],
                           stdin=cat.stdout,
                           stdout=subprocess.PIPE,
                        )
    end_of_pipe = grep.stdout
    for line in end_of_pipe:
        print line


def dfw_two():
    if re.match( r'^192.68.([1,6][^15,^8]).*', ipaddress, re.M|re.I):
       print "Cloud Two Region  #3"
       os.environ["OS_AUTH_URL"] = "http://cloudtwo-003-api-endpoint.prod.walmart.com:5000/v2.0/"
    else:
      print "Cloud Two Region  #4"
      os.environ["OS_AUTH_URL"] = "http:cloudtwo-004-api-endpoint.example.com:6000/v2.0/"
    cat = subprocess.Popen(['nova', 'list'],
                           stdout=subprocess.PIPE,
                        )
    grep = subprocess.Popen(['grep','-w', sys.argv[1]],
                           stdin=cat.stdout,
                           stdout=subprocess.PIPE,
                        )
    end_of_pipe = grep.stdout
    for line in end_of_pipe:
        print line



ipaddress = sys.argv[1]
if re.match( r'^102.60.16', ipaddress, re.M|re.I):
   dal_one()
elif re.match( r'^101.60', ipaddress, re.M|re.I):
   dal_two()
elif re.match( r'^192.62.3', ipaddress, re.M|re.I):
   dfw_one()
elif re.match( r'^192.68', ipaddress, re.M|re.I):
   dfw_two()
else:
   print "no match found"
