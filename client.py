import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ''

while True:
    msg = s.recv(1024)  # Defining the size of the data chunks, buffer size
    if len(msg) <= 0:
        break
    full_msg += msg.decode('utf-8')

print(msg.decode('utf-8'))
