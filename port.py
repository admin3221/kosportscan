from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
from sys import stdout
from threading import Thread
x11 = int(input('\n [ Enter x port 1... : '))
x22 = int(input(' [ Enter y port 65535... : '))
ip = input(' [ Enter ip : ')
sl = 0.01
print('\n')
def yel(ip, port):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		s.settimeout(20)
		s.connect((ip, port))
		print(f" [ OPEN : {ip}:{port} \r")
	except:
		pass
for _ in range(x11, x22):
		Thread(target=yel, args=[ip, _]).start()
		stdout.write(f" [ Checked : {_} \r")
		stdout.flush()
		sleep(sl)