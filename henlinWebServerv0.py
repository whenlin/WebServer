#import socket module
from socket import *
import http.server
import sys # In order to terminate the program
serverPort = 11000
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
#Fill in start
serverSocket.bind(('192.168.2.55', serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  
    try:
        message = connectionSocket.recv(1024).decode()  
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() 
        #Send one HTTP header line into socket
        #Fill in start
        responseMessage = 'HTTP/1.1 200 OK\nContent-Type: text/html'
        connectionSocket.send(responseMessage.encode('utf-8'))
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start 
        #Fill in end
        responseMessage = 'HTTP/1.1 404 File not found'
        connectionSocket.send(responseMessage.encode('utf-8'))
        connectionSocket.close()
        #Close client socket                             
        
        serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 