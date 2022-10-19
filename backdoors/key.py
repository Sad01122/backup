import socket
import json
import time

def maintain():
    cmd=input('Shell~* %s'%str("127.0.0.1:  "))
    jsoncmd=json.dumps(cmd)
    s.send(jsoncmd.encode())
def listen():
    try:
        s.bind(('192.168.10.9', 4444))
        s.listen()
        print("[+]  listening on port '4444'")
       sockobj, ip=s.accept()
       print(str(ip))
       print('[+]  Connected!')

        s.close()
    except:
        print("[-]  reconnecting...")
        time.sleep(2)
        listen()        
        
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen()

#maintain()



