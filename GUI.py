# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SMon = QtWidgets.QPushButton(self.centralwidget)
        self.SMon.setGeometry(QtCore.QRect(480, 490, 121, 61))
        self.SMon.setObjectName("SMon")
        self.GPUs = QtWidgets.QListWidget(self.centralwidget)
        self.GPUs.setGeometry(QtCore.QRect(10, 270, 351, 301))
        self.GPUs.setObjectName("GPUs")
        self.SelFil = QtWidgets.QPushButton(self.centralwidget)
        self.SelFil.setGeometry(QtCore.QRect(350, 27, 101, 31))
        self.SelFil.setObjectName("SelFil")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(10, 27, 311, 31))
        self.path.setInputMask("")
        self.path.setObjectName("path")
        self.SMine = QtWidgets.QPushButton(self.centralwidget)
        self.SMine.setGeometry(QtCore.QRect(460, 27, 101, 31))
        self.SMine.setObjectName("SMine")
        self.srv = QtWidgets.QLineEdit(self.centralwidget)
        self.srv.setGeometry(QtCore.QRect(100, 180, 261, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.srv.setFont(font)
        self.srv.setObjectName("srv")
        self.Acs = QtWidgets.QLineEdit(self.centralwidget)
        self.Acs.setGeometry(QtCore.QRect(10, 240, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Acs.setFont(font)
        self.Acs.setStyleSheet("color: rgb(0, 255, 0);")
        self.Acs.setObjectName("Acs")
        self.Rcs = QtWidgets.QLineEdit(self.centralwidget)
        self.Rcs.setGeometry(QtCore.QRect(190, 240, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Rcs.setFont(font)
        self.Rcs.setStyleSheet("color: rgb(255, 2, 2);")
        self.Rcs.setObjectName("Rcs")
        self.STMine = QtWidgets.QPushButton(self.centralwidget)
        self.STMine.setGeometry(QtCore.QRect(460, 60, 101, 31))
        self.STMine.setObjectName("STMine")
        self.Astart = QtWidgets.QCheckBox(self.centralwidget)
        self.Astart.setGeometry(QtCore.QRect(580, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Astart.setFont(font)
        self.Astart.setTristate(False)
        self.Astart.setObjectName("Astart")
        self.Muint = QtWidgets.QLineEdit(self.centralwidget)
        self.Muint.setGeometry(QtCore.QRect(570, 450, 141, 31))
        self.Muint.setObjectName("Muint")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 450, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.exeline = QtWidgets.QLineEdit(self.centralwidget)
        self.exeline.setGeometry(QtCore.QRect(10, 100, 731, 31))
        self.exeline.setObjectName("exeline")
        self.Tspeed = QtWidgets.QLineEdit(self.centralwidget)
        self.Tspeed.setGeometry(QtCore.QRect(100, 210, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Tspeed.setFont(font)
        self.Tspeed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Tspeed.setObjectName("Tspeed")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.urladd = QtWidgets.QLineEdit(self.centralwidget)
        self.urladd.setGeometry(QtCore.QRect(100, 150, 261, 20))
        self.urladd.setObjectName("urladd")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(580, 240, 131, 20))
        self.price.setObjectName("price")
        self.Nhashrate = QtWidgets.QLineEdit(self.centralwidget)
        self.Nhashrate.setGeometry(QtCore.QRect(580, 280, 131, 20))
        self.Nhashrate.setObjectName("Nhashrate")
        self.Ndiff = QtWidgets.QLineEdit(self.centralwidget)
        self.Ndiff.setGeometry(QtCore.QRect(580, 320, 131, 20))
        self.Ndiff.setObjectName("Ndiff")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 180, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(480, 240, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 280, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(500, 320, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(480, 380, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(210, 210, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.AVG = QtWidgets.QLineEdit(self.centralwidget)
        self.AVG.setGeometry(QtCore.QRect(250, 210, 113, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AVG.setFont(font)
        self.AVG.setObjectName("AVG")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI for EWBF miner"))
        self.SMon.setText(_translate("MainWindow", "Start monitor"))
        self.SelFil.setText(_translate("MainWindow", "Select start file"))
        self.path.setText(_translate("MainWindow", "Path to the file used to start miner"))
        self.SMine.setText(_translate("MainWindow", "Start mining"))
        self.srv.setText(_translate("MainWindow", "Not connected"))
        self.Acs.setText(_translate("MainWindow", "Accepted shares: 0"))
        self.Rcs.setText(_translate("MainWindow", "Rejected shares: 0"))
        self.STMine.setText(_translate("MainWindow", "Stop mining"))
        self.Astart.setText(_translate("MainWindow", "Auto restart"))
        self.Muint.setText(_translate("MainWindow", "30"))
        self.label.setText(_translate("MainWindow", "Monitor update interval (s):"))
        self.label_2.setText(_translate("MainWindow", "Path to the miner file:"))
        self.label_3.setText(_translate("MainWindow", "The execution line:"))
        self.Tspeed.setText(_translate("MainWindow", "0 Sol/s"))
        self.label_4.setText(_translate("MainWindow", "Listening:"))
        self.label_5.setText(_translate("MainWindow", "Server:"))
        self.label_6.setText(_translate("MainWindow", "Total speed:"))
        self.label_7.setText(_translate("MainWindow", "ZCASH network info"))
        self.label_8.setText(_translate("MainWindow", "Price (EUR):"))
        self.label_9.setText(_translate("MainWindow", "Network hashrate (MH/s):"))
        self.label_10.setText(_translate("MainWindow", "Difficulty:"))
        self.label_11.setText(_translate("MainWindow", "Monitoring"))
        self.label_12.setText(_translate("MainWindow", "AVG:"))
        self.AVG.setText(_translate("MainWindow", "0 Sol/s"))
