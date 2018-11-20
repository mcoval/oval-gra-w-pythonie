# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 80, 101, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton1"))
        self.pushButton2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(200, 160, 101, 50))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButton3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(200, 240, 101, 50))
        self.pushButton3.setObjectName(_fromUtf8("pushButton3"))

        self.pushButton4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(320, 80, 101, 50))
        self.pushButton4.setObjectName(_fromUtf8("pushButton4"))
        self.pushButton5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(320, 160, 101, 50))
        self.pushButton5.setObjectName(_fromUtf8("pushButton5"))
        self.pushButton6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(320, 240, 101, 50))
        self.pushButton6.setObjectName(_fromUtf8("pushButton6"))

        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 100, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 140, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 190, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(470, 170, 104, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(470, 40, 104, 71))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(190, 300, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(460, 360, 118, 22))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 260, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 340, 256, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(430, 450, 64, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(430, 510, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton2.setText(_translate("MainWindow", "PushButton2", None))
        self.pushButton3.setText(_translate("MainWindow", "PushButton3", None))
        self.pushButton4.setText(_translate("MainWindow", "PushButton4", None))
        self.pushButton5.setText(_translate("MainWindow", "PushButton5", None))
        self.pushButton6.setText(_translate("MainWindow", "PushButton6", None))
        self.radioButton.setText(_translate("MainWindow", "RadioButton", None))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton", None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

