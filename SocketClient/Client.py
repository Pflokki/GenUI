from threading import Thread, Timer
import socket
import json
from Messages import StopAttackMessage, StartAttackMessage, GetStatus, ClientStatus


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
            print("Wait data...")
            self.listen_socket()
        except ConnectionRefusedError:
            print("Problems while connecting, wait 10 sec")
            Timer(10, self.connect).start()
            self._reconnect = True

    def listen_socket(self):
        while True:
            data = self.receive_message()
            if len(data):
                print("o: {}".format(data))
                message = json.loads(data)
                if 't' in message:
                    if message['t'] == StartAttackMessage.tag:
                        self._window.start_attack()
                    elif message['t'] == StopAttackMessage.tag:
                        self._window.stop_attack()
                    elif message['t'] == GetStatus.tag:
                        self._send_status()

    def _send_status(self):
        status = ClientStatus()
        status.CPU = self._window.graph_creator.CPU
        status.RAM = self._window.graph_creator.RAM
        status.Connects = self._window.graph_creator.Connect
        status.Traffic = self._window.graph_creator.TrafficSum
        self.send_message(status.get_message())

    def send_message(self, message):
        self._socket.send(message)

    def receive_message(self):
        return self._socket.recv(20480).decode("UTF-8")
