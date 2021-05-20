#!/usr/bin/env python3
#phillij6@oregonstate.edu
#summer2020

#https://www.geeksforgeeks.org/socket-programming-python/
import socket
import sys
import argparse

def socketGet():
    print("Small Socket Get")
    #create a socket object and verify that it was succesfully created
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print ("Socket Succesfully created")
    except socket.error as err:
        print ("socket creation failed")
# set the port and host name and then connect it to the socket object
    port = 80
    host = 'gaia.cs.umass.edu'
    s.connect((host, port))
    print("socket successful on port: ", port) 
    print("Host:", host, "\n\n\n") 
       
    # set the get variable and send it encoded then receive a reply and decode it
    hostget = 'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
    s.sendall(hostget.encode())
    getreply = s.recv(1024).decode()
    s.close()
    #print the results 
    print("[RECV] - length:", len(getreply))
    print(getreply)
    #print(repr(getreply))


#https://stackoverflow.com/questions/49848375/how-to-use-python-socket-to-get-a-html-page
def getLarge():
    print("Get Large File")
     #create a socket object and verify that it was succesfully created
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket Succesfully created")
    except socket.error as err:
        print ("socket creation failed")
    # set the port and host name and then connect it to the socket object
    port = 80
    host = 'gaia.cs.umass.edu'
    s.connect((host, port))
    print("socket successful on port: ", port) 
    print("Host: ", host, "\n\n")  
     # set the get variable and send it encoded then receive a reply and decode it
    hostget = 'GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
    s.sendall(hostget.encode())
    #getreply = s.recv(1024).decode()
    #create a variable for the while loop when set to 0 it exits the while 
    dataInc = 1
    getreply = s.recv(1024).decode()
    fullreply = getreply
    while (dataInc != 0):
        #receive msg and add it to the full reply untill the reply received is empty
        getreply = s.recv(1024).decode()
        fullreply += getreply
        if not getreply:
           dataInc = 0

    s.close()
    print("[RECV] - length:", len(fullreply))
    print(fullreply)
    #print(repr(getreply))


#https://realpython.com/python-sockets/
def simpleHTTP():
    print("Simple HTTP")
     #create a socket object and verify that it was succesfully created
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket Succesfully created")
    except socket.error as err:
        print ("socket creation failed")
    # set the port and host name and then bind it to the socket object
    port = 1234
    host = '127.0.0.1' 
    s.bind((host, port))
    #s.connect((host, port))
    #the data we are to send
    data =  "HTTP/1.1 200 OK\r\n"\
                "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
                "<html>Congratulations!  You've downloaded the first Wireshark lab file!</html>\r\n"
    #object listens for a reply 
    s.listen()
    #waiting for the client connection
    conn, addr = s.accept()
    #close socket at the of the block
    with conn:
        print('Connected by:', addr, "\n")
        while True:
            #read the data received 
            getreply = conn.recv(1024)
            if not getreply:
                break
            print("Received: ", getreply, "\n")
            print("Sending>>>>>>>>>")
            #change str to bytes
            conn.sendall(bytes(data, 'utf8'))
            print(data)
            print("<<<<<<<<")
            s.close()
            break

    #print("[RECV] - length:", len(getreply))
    #print(getreply)

def main():
    print("Please choose a program to run enter the number you wish to run")
    
    userInput = input("1: Get File, 2: Get Large File, 3: Simple HTTP: ")
    print("You entered: ", userInput)

    if userInput == '1':
        socketGet()
    elif userInput == '2':
        getLarge()
    else:
        print("Start web browser at: 127.0.0.1:1234")
        simpleHTTP()

if __name__ == "__main__":
    main()