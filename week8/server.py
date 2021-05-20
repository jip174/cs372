#!/usr/bin/env python3
#https://realpython.com/python-sockets/
#https://docs.python.org/3.4/howto/sockets.html
import socket

def serverFunc():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65431        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            print('Type /q to quit')
            print('Waiting for message...')
            while True:
                data = conn.recv(1024).decode() #decodes reply
                if not data:
                    break
                print("" + str(data)) # print reply
                userIn = input("> ") #gets input from user
                conn.send(userIn.encode())
                if (userIn == '/q'): #quit the program if /q is enter
                    exit()
                    conn.close()

            conn.close()

if __name__ == '__main__':
    serverFunc()
