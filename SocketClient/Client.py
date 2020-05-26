from threading import Thread, Timer
import socket
import json
from Messages import StopAttackMessage, StartAttackMessage, GetStatus, ClientStatus, DieMessage


SERVER_ADDRESS = ('127.0.0.1', 8080)


class SocketClient(Thread):
    def __init__(self, window):
        super().__init__()
        print("Create connection")
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._window = window
        self._reconnect = False

    def run(self) -> None:
        self.connect()

    def reconnect(self):
        print("Problems while connecting, wait 10 sec")
        Timer(10, self.connect).start()
        self._reconnect = True

    def connect(self):
        print("Connect...")
        try:
            self._socket.connect(SERVER_ADDRESS)
            print("Wait data...")
            self.listen_socket()
        except ConnectionRefusedError:
            self.reconnect()

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
                    elif message['t'] == DieMessage.tag:
                        self._window.die()

    def _send_status(self):
        status = ClientStatus()
        status.cpu = self._window.graph_creator.cpu
        status.ram = self._window.graph_creator.ram
        status.connection_value = self._window.graph_creator.connection_value
        status.traffic_value = self._window.graph_creator.traffic_value
        self.send_message(status.get_message())

    def send_message(self, message):
        self._socket.send(message)

    def receive_message(self):
        return self._socket.recv(20480).decode("UTF-8")
