import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))  # Define end point for communication
s.listen()
print('Localhost server is running.')

while True:
	clientsocket, address = s.accept()
	print(f'Connection from {address} has been established.')
	clientsocket.send(bytes('Welcome to the server', 'utf-8'))
