################################################################
# Author        : Mounika Musugu <mounikamounika30m@gmail.com>
# Co Author     : Aravind Potluri <aravindswami135@gmail.com>
# Description   : This TCP based client, connects to TCP server
#                 to send and recevie Msgs in a loop.
################################################################

# Macros
serverIP = "127.0.0.1"  # Defaulting local IP
serverPORT = 8080       # Server Port

# Imports
import socket

# Creating socket
def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
        print("[+] Socket successfully created")
        return sock
    except:
        print(f"[-] Socket creation failed")
        sock.close()
        exit()

# Connect to the server
def connect_to_server(sock, serverIP, serverPORT):
    try:
        sock.connect((serverIP, serverPORT))
        print("[+] Successfully connected to server")
    except:
        print("[-] Connection failed")
        sock.close()
        exit()

# Data communication
def data_exchange(sock):
    while True:
        try:
            # Sending the user input to server
            sock.send(input("\n[#] Enter the msg: ").encode('UTF-8'))

            # Receive the response from server
            data = sock.recv(1024) # Assuming MAX data to be received is 1024 Bytes.
            if len(data) == 0:
                raise socket.error # Broken pipe error
            print(f"[#] Response from server: {data.decode('UTF-8')}")

        except KeyboardInterrupt:
            print(" [!] Client shutting down.")
            break

        except socket.error:
            print("[!] Connection closed by server")
            break

        except Exception as err:
            print(f"[!] {str(err)}")
            break

if __name__ == "__main__":
    # Creating the socket
    sock = create_socket()

    # Get server IP from user
    serverIP = input("\n[#] Enter server IP: ")

    # Connecting to server
    connect_to_server(sock, serverIP, serverPORT)

    # Start communication
    data_exchange(sock)

    # Closing the connection
    sock.close()
