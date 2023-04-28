import socket
import time
import random

serverip = '192.168.0.100'
port = 9000
buffsize = 4096

temperature = ['20.3','25.8','23.1','30.9']

for i in range(10):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    
    select = random.choice(temperature)
    server.send(select.encode('utf-8'))
    
    data_server = server.recv(buffsize).decode('utf-8')
    print('Data from server:', data_server)
    server.close()
    time.sleep(2)