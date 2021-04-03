import socket
 
def scan():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = input("Enter IP to scan: ")
        port = int(input("Port: "))
        s.connect((ip, port))
        print(port,"port is open.")
	scan()
    except:
        print(port,"port is closed.")
	scan()
scan()
