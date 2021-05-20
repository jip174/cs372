#!/usr/bin/python3
#https://realpython.com/python-sockets/
#https://docs.python.org/3.4/howto/sockets.html
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65431        # The port used by the server
def clientFunc():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Connected to:')
        print('Type /q to quit')
        print('Enter message to send...')
        userIn = input('>') #gets input from user
        while (userIn != '/q'):
            s.send(userIn.encode()) #encodes the data to send
            #s.sendall(b, userIn)
            data = s.recv(1024).decode() #decodes the received message
            if(data == '/q'): #quit the program if /q is enter
                exit()
                s.close()
            print(repr(data)) #prints reply
            userIn = input('>') #gets input from user

        s.close()

if __name__ == '__main__':
    clientFunc()