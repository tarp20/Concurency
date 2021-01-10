# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(436, 748)
        mainWindow.setStyleSheet("background-color: #22222e")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 451, 281))
        self.frame.setStyleSheet("background-color: #fb5b5d")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 281, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("exchanging.png"))
        self.label_2.setObjectName("label_2")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(30, 300, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(30, 380, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.input_amount.setText("")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(30, 460, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(30, 540, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 650, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Mshtakan")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"  color: white;\n"
"  background-color:#fb5b5d;\n"
"  border-radius: 30;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #fa4244\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "Currency Converter"))
        self.pushButton.setText(_translate("mainWindow", "Convert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
