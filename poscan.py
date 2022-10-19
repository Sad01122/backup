#!/bin/python3
print("*"*50)
print("""
██████   ██████  ███████  ██████  █████  ███    ██ 
██   ██ ██    ██ ██      ██      ██   ██ ████   ██ 
██████  ██    ██ ███████ ██      ███████ ██ ██  ██ 
██      ██    ██      ██ ██      ██   ██ ██  ██ ██ 
██       ██████  ███████  ██████ ██   ██ ██   ████ 
                    
""")
import sys
import time
import socket
		# Check all arguments	  "    poscan.py    -host     -Start_port      -End_port   "
if(len(sys.argv)!=4):
	print("invalid arguments!, type \"-h\" for help")
	exit()
if(sys.argv[1]=="-h" ):
	print("------>  poscan.py host/target/ip start_port end_port   <------")
	print("""For example:
			python3 poscan.py google.com 20 80 """)
	print("\n Exiting program..")
	sys.exit()
		# change abc.com to ipv4
try:
	target=socket.gethostbyname(sys.argv[1])	# Host ip
except:
	print("something went wrong")
	sys.exit()
print("-"*50)		#  banner target analyzed
print("Target Analyzed: ")
print (target)
print("-"*50)

start_time=int(time.time())
		# Ports
port1=int(sys.argv[2])
port2=int(sys.argv[3])
		# Scan ports
try:		
	for port in range(port1, port2+1):
		print("Scanning Port ", port)
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Socket conn for each port
		s.settimeout(1)
		con=s.connect_ex((target, port))		# Tuple
		if (con==0):
			f=print("Port {} is open".format(port))
			print(f)
		s.close()
except KeyboardInterrupt:	# ctrl + C
	print("\n Exiting program..")
	sys.exit()

end_time=int(time.time())
print("\nTime taken: ", end_time - start_time, "seconds")
print("*"*50)
