import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)  # Defining the size of the data chunks, buffer size
print(msg.decode('utf-8'))
