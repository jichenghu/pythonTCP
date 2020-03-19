
from socket import *

#serverName = '192.168.31.133'
serverName = 'localhost'
serverPort = 12000

quit_cmd   = 'quit'
while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    sentence = input("input lowercase sentence:")

    if sentence == quit_cmd:
        break

    clientSocket.send(sentence.encode())

    modifiedSentence = clientSocket.recv(1024)
    print("From Server:", modifiedSentence.decode())

    clientSocket.close()


