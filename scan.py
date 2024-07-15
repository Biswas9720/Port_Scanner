#!/usr/bin/python3

import time
import socket
import sys
import threading


usage = " python3 scan.py TARGET START_PORT END_PORT "
print("-"*70)
print("Python Simple Port Scanner")
print("*"*70)

start_time = time.time()


if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:        #get address info 
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning Target",target)

def scan_port(port):

    #print("Scanning port ",port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    cons = s.connect_ex((target , port))  #not to close program _ex
    if(cons == 0):
        print("Port {} is open".format(port))
    s.close()

for port in range(start_port,end_port+1):

    thread = threading.Thread(target = scan_port , args= (port,))
    thread.start()

end_time = time.time()
print("Time taken:", end_time , start_time)

