from PyQt5.QtWidgets import QApplication
from uiControl.MainWindowControl import MainWindowControl
from SocketClient.Client import SocketClient


def main():
    app = QApplication([])
    window = MainWindowControl()
    tcp_client = SocketClient(window)
    tcp_client.start()
    window.show()
    app.exec_()
    tcp_client.join()


if __name__ == '__main__':
    main()
