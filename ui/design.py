# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 703)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 881, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_generate_data = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_generate_data.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_generate_data.setFont(font)
        self.pushButton_generate_data.setObjectName("pushButton_generate_data")
        self.horizontalLayout.addWidget(self.pushButton_generate_data)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_save_data = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_save_data.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save_data.setFont(font)
        self.pushButton_save_data.setObjectName("pushButton_save_data")
        self.horizontalLayout.addWidget(self.pushButton_save_data)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_generate_attack = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_generate_attack.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_generate_attack.setFont(font)
        self.pushButton_generate_attack.setObjectName("pushButton_generate_attack")
        self.horizontalLayout.addWidget(self.pushButton_generate_attack)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 881, 551))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget.setObjectName("widget")
        self.MplWidget_CPU = MplWidget(self.widget)
        self.MplWidget_CPU.setGeometry(QtCore.QRect(10, 10, 421, 261))
        self.MplWidget_CPU.setObjectName("MplWidget_CPU")
        self.MplWidget_Traffic = MplWidget(self.widget)
        self.MplWidget_Traffic.setGeometry(QtCore.QRect(0, 280, 431, 261))
        self.MplWidget_Traffic.setObjectName("MplWidget_Traffic")
        self.MplWidget_RAM = MplWidget(self.widget)
        self.MplWidget_RAM.setGeometry(QtCore.QRect(450, 10, 421, 261))
        self.MplWidget_RAM.setObjectName("MplWidget_RAM")
        self.MplWidget_Connects = MplWidget(self.widget)
        self.MplWidget_Connects.setGeometry(QtCore.QRect(450, 280, 421, 261))
        self.MplWidget_Connects.setObjectName("MplWidget_Connects")
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        self.Actions = QtWidgets.QMenu(self.menubar)
        self.Actions.setObjectName("Actions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setObjectName("New")
        self.Clear = QtWidgets.QAction(MainWindow)
        self.Clear.setObjectName("Clear")
        self.About = QtWidgets.QAction(MainWindow)
        self.About.setObjectName("About")
        self.Actions.addAction(self.About)
        self.menubar.addAction(self.Actions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_generate_data.setText(_translate("MainWindow", "Сгенерировать \n"
"данные\n"
""))
        self.pushButton_save_data.setText(_translate("MainWindow", "Записать \n"
"данные\n"
""))
        self.pushButton_generate_attack.setText(_translate("MainWindow", "Сгенерировать \n"
"атаку\n"
""))
        self.Actions.setTitle(_translate("MainWindow", "Меню"))
        self.New.setText(_translate("MainWindow", "Создать новый сценарий"))
        self.Clear.setText(_translate("MainWindow", "Очистить сценарий"))
        self.About.setText(_translate("MainWindow", "О программе"))

from mplwidget import MplWidget
