# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rand_gen.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import string
import random
import time

global s
y = int()
b = str()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(830, 370)
        MainWindow.setMinimumSize(QtCore.QSize(824, 351))
        MainWindow.setBaseSize(QtCore.QSize(200, 200))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "border-radius: 20px;\n"
                                 "}")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0.318, y1:0.25, x2:0.876, y2:0.909591, stop:0 rgba(0, "
            "147, 233, 255), stop:1 rgba(128, 208, 199, 255))")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                 "color: #fff;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 220, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: rgba(0, 0, 0, 0);\n"
                                   "color: #fff;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 651, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(22)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background:#fff;\n"
                                    "border:none;\n"
                                    "border-radius:35px;\n"
                                    "padding-left:30px;\n"
                                    "\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 260, 651, 71))
        self.textBrowser.setStyleSheet("background: #fff;\n"
                                       "border:none;\n"
                                       "border-radius:35px;\n"
                                       "padding-left:30px;\n"
                                       "font-size:30px;\n"
                                       "padding-top:10px;\n"
                                       "vertical-align:middle;\n")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 160, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.369, x2:0.988636, y2:0.903, stop:0 rgba(146, "
            "254, 157, 255), stop:1 rgba(0, 201, 255, 255));\n "
            "color: #fff;\n"
            "cursor:pointer;\n"
            "border-radius: 20px;\n"
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.textBrowser.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        f = 0
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random Password Generator"))
        self.label.setText(_translate("MainWindow", "How long should the password be?(Enter a number)"))
        self.label_2.setText(_translate("MainWindow", "Here\'s your password:"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))

        def func():

            def Rand_Generator():
                return ''.join(
                    random.choice("@" + "#" + string.ascii_letters + string.digits + string.hexdigits) for _ in
                    range(int(self.lineEdit.text())))

            def check_inp():
                try:
                    Rand_Generator()
                    return True
                except ValueError:
                    return False

            def main_1():
                g = check_inp()
                if g:
                    a = Rand_Generator()
                    self.textBrowser.setText(_translate("MainWindow", a))
                else:
                    self.textBrowser.setText(_translate("MainWindow", "Please Enter a Number Only"))
                self.lineEdit.setText(_translate("MainWindow", ""))

            self.pushButton.clicked.connect(main_1)
        func()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
