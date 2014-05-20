#! /usr/bin/python2.7
import sys
import os
#Export variable for Nova access
#~sid 

with open('sample.sh', 'r') as file:
    data = file.readlines()
data[0] = 'export OS_AUTH_URL=' + sys.argv[1] + '\n'
with open('sample.sh', 'w') as file:
    file.writelines( data )
file.close()
os.system("source sample.sh")
