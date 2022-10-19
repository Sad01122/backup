#!/bin/python3
print(""" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
          ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌     ▐░▌  
 ▄▄▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                           """)


import subprocess
import re
def label():
	print("-"*50)
MAC = ""
new_mac="A8:40:ED:F7:AC:C3"
label()
		# MAC changer
print("""▁ ▂ ▄ ▅ ▆ ▇ █ MAC CHANGER █ ▇ ▆ ▅ ▄ ▂ ▁""")
label()
iface=input("Enter your interface: ")
def mac_prepare():
	output = subprocess.run(["ifconfig", iface], capture_output=True)#run ifconfig and capture output
	plained = output.stdout.decode(' utf-8 ')	#decode into utf-8
	# search mac
	pattern=r'ether\s[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}'#raw string 	notation
	compiled=re.compile(pattern)		# execute pattern   : )
	#print(compiled)		# for learning pupose

	ans=compiled.search(plained)
	current_mac=ans.group().split(" ")[1]
	MAC=current_mac
	print("current mac: ", MAC)

mac_prepare()
print(MAC)


			#Change MAC Now!!



cmd_down = subprocess.run(["ifconfig", iface, "down"], capture_output=True)
cmd_change = subprocess.run(["ifconfig", iface, "hw", "ether", new_mac], capture_output=True)
out = cmd_change.stdout.decode(' utf-8 ')
cmd_up = subprocess.run(["ifconfig", iface, "up"], capture_output=True)
#print(cmd_change)
print("[+]   New MAC address will " + new_mac)


			# Success or NOT
exe_ifcon = subprocess.run(["ifconfig", iface], capture_output=True)#run ifconfig and capture output
plained = exe_ifcon.stdout.decode(' utf-8 ')
print(plained)
cpattern=r'ether\s[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}'#raw string 
com_cpat=re.compile(cpattern)
result=com_cpat.search(plained)
now_mac=result.group().split(" ")[1]
compare=now_mac
print(compare)
label()

print("------>    Now your MAC address is ", now_mac)
if new_mac==compare:
	print("[!]  Not changed.. Type 'sudo' while running")


