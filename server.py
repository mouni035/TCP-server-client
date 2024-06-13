################################################################
# Author        : Mounika Musugu <mounikamounika30m@gmail.com>
# Co Author     : Aravind Potluri <aravindswami135@gmail.com>
# Description   : This TCP based server, waits for TCP client
#                 Msgs and then sends our Msg in loop.
################################################################

# Macros
serverIP = "0.0.0.0"    # Accept from any IP.
serverPORT = 8080       # Server Port  

# Imports
import socket

# Create socket
def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
        print("[+] Socket successfully created")
        return sock
    except:
        print(f"[-] Socket creation failed")
        sock.close()
        exit()

# Bind socket
def bind_socket(sock, serverIP, serverPORT):
    try:
        sock.bind((serverIP, serverPORT))
        print(f"[+] socket successfully binded on port {serverPORT}")
    except:
        print(f"[-] Socket binding failed")	
        sock.close()
        exit()

# Establishing the connection
def listen_for_connections(sock):
    try:
        sock.listen(2)
        print("[+] wating for connection...")
        clientSock, clientAddr = sock.accept()
        print(f"[+] Accepted connection from : {clientAddr}\n")
        return clientSock
    except:
        print("[-] Connection establishment faild")
        sock.close()
        exit()

# Data communication
def data_exchange(sock, clientSock):
    while True:
        try:
            # Receive data from any client
            data = clientSock.recv(1024) # Assuming MAX data to be received is 1024 Bytes.
            if len(data) == 0:
                raise socket.error # To escape the infinte loop, after breaking the tcp pipeline
            msg = data.decode('UTF-8')
            print(f"[#] Received message: {msg}")

            # Reply msg to client
            msg = input("\n[#] Enter the msg: ")
            clientSock.send(msg.encode('UTF-8'))

        except KeyboardInterrupt:
            print(" [!] Server shutting down.")
            break

        except socket.error:
            print("[!] Connection closed by client")
            break

        except Exception as err:
            print(f"[!] {str(err)}")
            break

if __name__ == "__main__":
    # Creating socket
    sock = create_socket()

    # Bind socket
    bind_socket(sock, serverIP, serverPORT)

    # Wait for connections
    clientSock = listen_for_connections(sock)

    # Data exchange
    data_exchange(sock, clientSock)

    # Closing the connection
    sock.close()