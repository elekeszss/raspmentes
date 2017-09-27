import socket
import threading
from blink import relayon1,relayoff1,relayon2,relayoff2

bind_ip = '192.168.0.100'
bind_port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print 'Listening on {}:{}'.format(bind_ip, bind_port)


def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    if request == 'ON1':
        relayon1()
        client_socket.send('Relay 1 is ON')
        client_socket.close()
    if request == 'ON2':
        relayon2()
        client_socket.send('Relay 2 is ON')
        client_socket.close()
    if request == 'OFF1':
        relayoff1()
        client_socket.send('Relay 1 is OFF')
        client_socket.close()
    if request == 'OFF2':
        relayoff2()
        client_socket.send('Relay 2 is OFF')
        client_socket.close()   
        
        
    print 'Received {}'.format(request)


while True:
    client_sock, address = server.accept()
    print 'Accepted connection from {}:{}'.format(address[0], address[1])
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()
    print("ok")