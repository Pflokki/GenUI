from threading import Thread, Timer
import socket
import json
from Messages import StopAttackMessage, StartAttackMessage


SERVER_ADDRESS = ('127.0.0.1', 8080)


class ClientSocket(Thread):
    def __init__(self, window):
        super().__init__()
        print("Create connection")
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._window = window
        self._reconnect = False

    def run(self) -> None:
        self.connect()

    def connect(self):
        print("Connect...")
        try:
            self._socket.connect(SERVER_ADDRESS)
        except ConnectionRefusedError:
            print("Problems while connecting, wait 10 sec")
            Timer(10, self.connect).start()
            self._reconnect = True

        else:
            self.listen_socket()

    def listen_socket(self):
        while True:
            print("Wait data...")
            data = self.receive_message()
            if len(data):
                print("o: {}".format(data))
                message = json.loads(data)
                if 't' in message:
                    if message['t'] == StartAttackMessage().tag:
                        self._window.start_attack()
                    elif message['t'] == StopAttackMessage().tag:
                        self._window.stop_attack()

    def receive_message(self):
        return self._socket.recv(2048).decode("UTF-8")
