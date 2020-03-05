import random
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi

from uiControl.InfoWindowControl import InfoWindow

from GraphCreator import GraphCreator


class MainWindowControl(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("./ui/design.ui", self)

        self.setWindowTitle("Генератор данных")
        self.graph_creator = GraphCreator()
        self.info_window = InfoWindow()
        self.init_plot()

        self.generator_started = False
        self._attack_length = 0
        self._normal_length = 50
        self.pushButton_generate_data.clicked.connect(self.start_printing)
        # self.pushButton_generate_attack.clicked.connect(self.generate_attack)
        self.pushButton_save_data.clicked.connect(self.write_to_file)
        self.About.triggered.connect(self.show_info_window)

        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self.update_graph)

    def show_info_window(self):
        self.info_window.show()

    def start_printing(self):
        if self.generator_started:
            self.plot_timer.stop()
            self.generator_started = False
        else:
            self.plot_timer.start(1)
            self.generator_started = True

    def update_graph(self):
        if self._attack_length:
            self._attack_length -= 1
            self.generate_attack()
        else:
            if random.randint(0, 100) < 5:
                self._attack_length = random.randint(30, 150)
            self.generate_normal()

    def generate_normal(self):
        self.graph_creator.update_graph()
        MainWindowControl.plotting_pictures(self)
        # self.io_loop.add_timeout(self.io_loop.time() + 2, self.update_graph)

    def generate_attack(self):
        self.graph_creator.generate_attack()
        MainWindowControl.plotting_pictures(self)  # plotting attack plots

    def init_plot(self):
        self.MplWidget_CPU.canvas.axes.set_title('Нагрузка ЦП, %')
        self.MplWidget_CPU.canvas.axes.set_xlabel('Время, с')
        self.MplWidget_CPU.canvas.axes.set_ylabel("Процент загрузки, %")
        self.MplWidget_CPU.canvas.axes.set_ylim(0, 100, 1)

        self.MplWidget_RAM.canvas.axes.set_title('Нагрузка ОЗУ, %')
        self.MplWidget_RAM.canvas.axes.set_xlabel('Время, с')
        self.MplWidget_RAM.canvas.axes.set_ylabel("Процент загрузки, %")
        self.MplWidget_RAM.canvas.axes.set_ylim(0, 100, 1)

        self.MplWidget_Connects.canvas.axes.set_title('Установленные соединения, %')
        self.MplWidget_Connects.canvas.axes.set_xlabel('Время, с')
        self.MplWidget_Connects.canvas.axes.set_ylabel("Процент соединений, %")
        self.MplWidget_Connects.canvas.axes.set_ylim(0, 100, 1)

        self.MplWidget_Traffic.canvas.axes.set_title('Суммарный объем сетевого трафика, пак/с')
        self.MplWidget_Traffic.canvas.axes.set_xlabel('Время, с')
        self.MplWidget_Traffic.canvas.axes.set_ylabel("Количество пакетов")

    def plotting_pictures(self):
        self.MplWidget_CPU.canvas.axes.clear()
        self.MplWidget_RAM.canvas.axes.clear()
        self.MplWidget_Connects.canvas.axes.clear()
        self.MplWidget_Traffic.canvas.axes.clear()

        self.init_plot()

        self.MplWidget_CPU.canvas.axes.plot(self.graph_creator.CPU)
        self.MplWidget_RAM.canvas.axes.plot(self.graph_creator.RAM)
        self.MplWidget_Connects.canvas.axes.plot(self.graph_creator.Connect)
        self.MplWidget_Traffic.canvas.axes.plot(self.graph_creator.TrafficSum)

        self.MplWidget_CPU.canvas.draw()
        self.MplWidget_RAM.canvas.draw()
        self.MplWidget_Connects.canvas.draw()
        self.MplWidget_Traffic.canvas.draw()

    def write_to_file(self):
        self.graph_creator.write_to_file()
