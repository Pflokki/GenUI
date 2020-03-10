from threading import Thread
import socket


SERVER_ADDRESS = ('127.0.0.1', 8080)


class ClientSocket(Thread):
    def __init__(self, window):
        super().__init__()
        print("Create connection")
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._window = window

    def run(self) -> None:
        print("Connect...")
        self._socket.connect(SERVER_ADDRESS)

        while True:
            print("Wait data...")
            data = self.receive_message()
            print("o: {}".format(data))

    def receive_message(self):
        data = self._socket.recv(2048).decode("UTF-8")
        if len(data):
            if data[:-1] == "Start attack":
                self._window.start_attack()
            elif data[:-1] == "Stop attack":
                self._window.stop_attack()
        return data[:-1]
