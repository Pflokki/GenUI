from PyQt5.QtWidgets import QApplication
from uiControl.MainWindowControl import MainWindowControl
from SocketClient.Client import ClientSocket
import sys


def main():
    app = QApplication([])
    window = MainWindowControl()
    tcp_client = ClientSocket(window)
    tcp_client.start()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
