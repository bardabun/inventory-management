import socket
import communication_file


DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
HEADER = 64
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
cf = communication_file.ClientCommunication(PORT, FORMAT, HEADER, SERVER)
cf.connect_socket()
while True:
    try:
        print(cf.send_received(input()))
    except:
        print("the connection is over - do you want to connect again ?")
        if input() != "yes":
            break
        cf.connect_socket()


