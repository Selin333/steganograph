# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1156, 697)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.original_image = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.original_image.setGeometry(QtCore.QRect(710, 80, 441, 271))
        self.original_image.setObjectName("original_image")
        self.stego_image = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.stego_image.setGeometry(QtCore.QRect(710, 360, 441, 271))
        self.stego_image.setObjectName("stego_image")
        self.textEdit_message = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_message.setGeometry(QtCore.QRect(10, 20, 1141, 51))
        self.textEdit_message.setObjectName("textEdit_message")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 0, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stego_metod = QtWidgets.QComboBox(parent=self.centralwidget)
        self.stego_metod.setGeometry(QtCore.QRect(170, 275, 341, 31))
        self.stego_metod.setObjectName("stego_metod")
        self.stego_metod.addItem("")
        self.stego_metod.addItem("")
        self.stego_metod.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button_hide_message = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_hide_message.setGeometry(QtCore.QRect(20, 580, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_hide_message.setFont(font)
        self.button_hide_message.setObjectName("button_hide_message")
        self.button_extract_message = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_extract_message.setGeometry(QtCore.QRect(370, 580, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_extract_message.setFont(font)
        self.button_extract_message.setObjectName("button_extract_message")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit_m_start = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_m_start.setGeometry(QtCore.QRect(30, 140, 161, 31))
        self.textEdit_m_start.setObjectName("textEdit_m_start")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_m_end = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_m_end.setGeometry(QtCore.QRect(410, 140, 151, 31))
        self.textEdit_m_end.setObjectName("textEdit_m_end")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 410, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_sdvig = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_sdvig.setGeometry(QtCore.QRect(360, 405, 151, 31))
        self.textEdit_sdvig.setObjectName("textEdit_sdvig")
        self.stego_reid = QtWidgets.QComboBox(parent=self.centralwidget)
        self.stego_reid.setGeometry(QtCore.QRect(180, 405, 101, 31))
        self.stego_reid.setObjectName("stego_reid")
        self.stego_reid.addItem("")
        self.stego_reid.addItem("")
        self.stego_reid.addItem("")
        self.stego_reid.addItem("")
        self.stego_reid.addItem("")
        self.stego_reid.addItem("")
        self.stego_reid.addItem("")
        self.stego_reid.addItem("")
        self.stego_reid.addItem("")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 410, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 190, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(600, 470, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAcceptDrops(False)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.open_new_container = QtGui.QAction(parent=MainWindow)
        self.open_new_container.setObjectName("open_new_container")
        self.save_file = QtGui.QAction(parent=MainWindow)
        self.save_file.setObjectName("save_file")
        self.exit = QtGui.QAction(parent=MainWindow)
        self.exit.setObjectName("exit")
        self.autor = QtGui.QAction(parent=MainWindow)
        self.autor.setObjectName("autor")
        self.open_full_container = QtGui.QAction(parent=MainWindow)
        self.open_full_container.setObjectName("open_full_container")
        self.menu.addAction(self.open_new_container)
        self.menu.addAction(self.open_full_container)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stego_metod.setCurrentIndex(0)
        self.stego_reid.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Селин лаб9"))
        self.label.setText(_translate("MainWindow", "Введите скрываемое сообщение:"))
        self.stego_metod.setItemText(0, _translate("MainWindow", "LSB-R"))
        self.stego_metod.setItemText(1, _translate("MainWindow", "LSB-M"))
        self.stego_metod.setItemText(2, _translate("MainWindow", "Код Хемминга"))
        self.label_3.setText(_translate("MainWindow", "Метод:"))
        self.button_hide_message.setText(_translate("MainWindow", "Внедрить сообщение в контейнер"))
        self.button_extract_message.setText(_translate("MainWindow", "Извлечь сообщение из контейнера"))
        self.label_4.setText(_translate("MainWindow", "Начальная метка"))
        self.label_5.setText(_translate("MainWindow", "Конечная метка"))
        self.label_6.setText(_translate("MainWindow", "Рейд внедрения:"))
        self.stego_reid.setItemText(0, _translate("MainWindow", "3"))
        self.stego_reid.setItemText(1, _translate("MainWindow", "1.5"))
        self.stego_reid.setItemText(2, _translate("MainWindow", "1"))
        self.stego_reid.setItemText(3, _translate("MainWindow", "0.75"))
        self.stego_reid.setItemText(4, _translate("MainWindow", "0.5"))
        self.stego_reid.setItemText(5, _translate("MainWindow", "0.25"))
        self.stego_reid.setItemText(6, _translate("MainWindow", "0.2"))
        self.stego_reid.setItemText(7, _translate("MainWindow", "0.1"))
        self.stego_reid.setItemText(8, _translate("MainWindow", "0.05"))
        self.label_7.setText(_translate("MainWindow", "Сдвиг:"))
        self.label_8.setText(_translate("MainWindow", "Оригинал"))
        self.label_9.setText(_translate("MainWindow", "Заполненный контейнер"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.open_new_container.setText(_translate("MainWindow", "Создать"))
        self.save_file.setText(_translate("MainWindow", "Сохранить"))
        self.exit.setText(_translate("MainWindow", "Выйти"))
        self.autor.setText(_translate("MainWindow", "Автор"))
        self.open_full_container.setText(_translate("MainWindow", "Открыть"))
