# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rshang\Desktop\ABC.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 386)
        MainWindow.setMinimumSize(QtCore.QSize(603, 386))
        MainWindow.setMaximumSize(QtCore.QSize(603, 386))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 61, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 140, 71, 51))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 220, 551, 101))
        self.listWidget.setObjectName("listWidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 110, 461, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_inout = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_inout.setObjectName("lineEdit_inout")
        self.horizontalLayout.addWidget(self.lineEdit_inout)
        self.toolButto_input = QtWidgets.QToolButton(self.widget)
        self.toolButto_input.setObjectName("toolButto_input")
        self.horizontalLayout.addWidget(self.toolButto_input)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 170, 461, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_output = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.horizontalLayout_2.addWidget(self.lineEdit_output)
        self.toolButton_output = QtWidgets.QToolButton(self.widget1)
        self.toolButton_output.setObjectName("toolButton_output")
        self.horizontalLayout_2.addWidget(self.toolButton_output)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolButto_input.clicked.connect(MainWindow.UIpath)
        self.toolButton_output.clicked.connect(MainWindow.PYpath)
        self.pushButton.clicked.connect(MainWindow.Push)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pyqt .UI to .PY tool"))
        self.label_2.setText(_translate("MainWindow", "From .UI path"))
        self.label_3.setText(_translate("MainWindow", "To .py path"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.toolButto_input.setText(_translate("MainWindow", "..."))
        self.toolButton_output.setText(_translate("MainWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

