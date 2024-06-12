import socket
try:
    server_hostname = socket.gethostname()
    server_ip = socket.gethostbyname(server_hostname)
    s = socket.socket()
    s.connect((server_ip,8080))
    while True:
        msg=input("enter client msg: ")
        s.send(bytes(msg,'utf-8'))
        recvmsg=s.recv(1024).decode()
        print(recvmsg)
except socket.error as err:
    print(f"Socket error: {err}")
finally:
    s.close()


