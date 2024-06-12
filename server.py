import socket
try:
    s = socket.socket()
    print("socket created")
    server_ip = ''
    s.bind((server_ip,8080))
    while True:
        s.listen(3)
        print("waiting for connection")
        client,addr=s.accept()
        print(addr)
        recvmsg= client.recv(1024).decode()
        print("received message: ",recvmsg)
        msg=input("enter message from server: ")
        client.send(bytes(msg,'utf-8'))
except socket.error as err:
    print(f"Socket error: {err}")
finally:
    client.close()