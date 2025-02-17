import random
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi

from uiControl.InfoWindowControl import InfoWindow

from TrafficCreator.WebTrafficCreator import WebTrafficCreator


class MainWindowControl(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("./ui/design.ui", self)

        self.setWindowTitle("Генератор данных")
        self.graph_creator = WebTrafficCreator()
        self.info_window = InfoWindow()
        self.init_plot()

        self.generator_started = False
        self._attack_length = 0
        self._normal_length = 50
        self.is_attack = False
        self.is_die = False
        self.set_warning_text()
        # self.pushButton_generate_data.clicked.connect(self.start_printing)
        # self.pushButton_generate_attack.clicked.connect(self.generate_attack)
        self.pushButton_save_data.clicked.connect(self.write_to_file)
        self.About.triggered.connect(self.show_info_window)

        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self.update_graph)

        self.start_printing()

    def show_info_window(self):
        self.info_window.show()

    def show_warning_window(self):
        self.warning_window.show()

    def start_printing(self):
        if self.generator_started:
            self.plot_timer.stop()
            self.generator_started = False
        else:
            self.plot_timer.start(1)
            self.generator_started = True

    def update_graph(self):
        if self.is_die:
            self.generate_die_data()
        else:
            if self.is_attack:
                self.generate_attack()
            else:
                self.generate_normal()

    def start_attack(self):
        self.is_attack = True
        self.set_warning_text()

    def stop_attack(self):
        self.is_attack = False
        self.set_warning_text()

    def die(self):
        self.is_die = True
        self.set_warning_text()

    def set_warning_text(self):
        if self.is_die:
            self.l_warning.setText("Внмание! Устройство не отвечает.")
        else:
            if self.is_attack:
                self.l_warning.setText("Внмание! На данное устройство производится DDoS-аттака.")
            else:
                self.l_warning.setText("Устройство работает в нормальном режиме.")

    def manual_update_graph(self):
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

    def generate_die_data(self):
        self.graph_creator.generate_die_data()
        MainWindowControl.plotting_pictures(self)  # plotting die plots

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

        self.MplWidget_CPU.canvas.axes.plot(self.graph_creator.cpu)
        self.MplWidget_RAM.canvas.axes.plot(self.graph_creator.ram)
        self.MplWidget_Connects.canvas.axes.plot(self.graph_creator.connection_value)
        self.MplWidget_Traffic.canvas.axes.plot(self.graph_creator.traffic_value)

        self.MplWidget_CPU.canvas.draw()
        self.MplWidget_RAM.canvas.draw()
        self.MplWidget_Connects.canvas.draw()
        self.MplWidget_Traffic.canvas.draw()

    def write_to_file(self):
        train_data, train_predicate = self.graph_creator.train_data_formatter()
        self.graph_creator.write_to_file(
            train_data, train_predicate
        )
