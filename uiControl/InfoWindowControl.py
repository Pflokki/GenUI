from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class InfoWindow(QWidget):
    def __init__(self):
        info = "Данный программный продукт является моделью поведения сетевого узла-жертвы при нормальных условиях \n" \
               "и в момент проведения атаки. Предназначен для генерации исходных данных, используемых в обучении \n" \
               "искусственной нейронной сети."
        super(InfoWindow, self).__init__()
        self.setWindowTitle('О программе')
        self.setFixedSize(640, 480)
        self.label = QLabel(self)
        self.label.setText(info)
        #        self.label.setAlignment(AlignCenter)

        widget = QWidget(self)
        layout = QVBoxLayout(widget)
        layout.addWidget(self.label)

