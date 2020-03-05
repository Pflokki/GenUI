from PyQt5.QtWidgets import QApplication
from uiControl.MainWindowControl import MainWindowControl


def main():
    app = QApplication([])
    window = MainWindowControl()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
