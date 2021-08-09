import socket
import threading


class Communication:
    def __init__(self, port, format, header_size, server_add):
        self.PORT = port
        self.HEADER_SIZE = header_size
        self.FORMAT = format
        self.SERVER_ADD = server_add
        self.socket = None

    def get_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self.socket

    def get_addr(self):
        addr = (self.SERVER_ADD, self.PORT)
        return addr

    def get_send(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER_SIZE - len(send_length))
        return message, send_length


class ServerCommunication(Communication):
    def __init__(self, port, format, header_size, server_add):
        Communication.__init__(self, port, format, header_size, server_add)
        self.socket = None

    def send(self, msg, conn):
        message, send_length = Communication.get_send(self, msg)
        conn.send(send_length)
        conn.send(message)

    def received(self, conn):
        while True:
            msg_length = conn.recv(self.HEADER_SIZE).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)
                return msg

    def send_received(self, msg, conn):
        self.send(msg, conn)
        return self.received(conn)

    def start(self, threads_func):
        server = self.get_socket()
        server.bind(self.get_addr())
        print("Server Start Listening")
        server.listen()
        while True:
            conn, addr = server.accept()
            print("got a new connection")
            thread = threading.Thread(target=threads_func, args=(conn, addr, self))
            thread.start()


class ClientCommunication(Communication):
    def __init__(self, port, format, header_size, server_add):
        Communication.__init__(self, port, format, header_size, server_add)

    def send(self, msg):
        message, send_length = Communication.get_send(self, msg)
        self.socket.send(send_length)
        self.socket.send(message)

    def received(self):
        while True:
            msg_length = self.socket.recv(self.HEADER_SIZE).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.socket.recv(msg_length).decode(self.FORMAT)
                return msg

    def send_received(self, msg):
        self.send(msg)
        return self.received()

    def connect_socket(self):
        self.get_socket().connect(self.get_addr())
