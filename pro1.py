#!/usr/bin/python
#https://www.geeksforgeeks.org/socket-programming-python/
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket Succesfully created")
except socket.error as err:
    print ("socket creation failed")

port = 80
host = 
try:
    #hostget = socket.gethostbyname('GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n')
    hostget = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("error retrieving host name")
    sys.exit()

s.connect((hostget, port))
print("socket successful on port:", port) 