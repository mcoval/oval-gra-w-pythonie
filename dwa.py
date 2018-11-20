import sys, os
import time
import webbrowser
import pyautogui
import win32gui
import time


from PyQt4 import QtCore, QtGui

# import klasy
from testui import Ui_MainWindow


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.zrobcos1)
        QtCore.QObject.connect(self.ui.pushButton2, QtCore.SIGNAL("clicked()"), self.zrobcos2)
        QtCore.QObject.connect(self.ui.pushButton3, QtCore.SIGNAL("clicked()"), self.zrobcos3)
        QtCore.QObject.connect(self.ui.pushButton4, QtCore.SIGNAL("clicked()"), self.zrobcos4)
        QtCore.QObject.connect(self.ui.pushButton5, QtCore.SIGNAL("clicked()"), self.zrobcos5)
        QtCore.QObject.connect(self.ui.pushButton6, QtCore.SIGNAL("clicked()"), self.zrobcos6)

    def zrobcos1(self):
        self.ui.pushButton.setText('aaaaaaaaaa')
        for x in range(5):
            time.sleep(0.2)
            self.ui.textEdit.setText("bblabla " + str(x))
            self.ui.lcdNumber.display(x)
            self.ui.progressBar.setProperty("value", x)
        self.wiadomosc("costam")


    def wiadomosc(self, tekst):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setText(tekst)
        msgBox.setInformativeText(self.ui.plainTextEdit.toPlainText())
        msgBox.addButton(QtGui.QMessageBox.Ok)
        ret = msgBox.exec_()

        if ret == QtGui.QMessageBox.Yes:
            self.ui.textEdit.setText("yesssss")
            return
        else:
            self.ui.textEdit.setText("nooooooo")
            return

    def zrobcos2(self):
        time.sleep(2)
        w = win32gui
        asd = w.GetWindowText(w.GetForegroundWindow())

        self.wiadomosc(asd)

    def zrobcos3(self):
        adres = self.ui.textEdit.toPlainText()
        cpu = os.system('ping ' + adres)
        if cpu == 0:
            self.ui.textEdit.setText("strona odpowiada")
        else:
            self.ui.textEdit.setText("strona nie działa")

    def zrobcos4(self):
        lista = os.listdir("C:/Users/oval/Desktop/test")
        print(*lista, sep=", ")


    def zrobcos5(self):
        pyautogui.moveRel(10, 20, 0.26)
        pyautogui.click()
        pyautogui.typewrite("hey there", interval=0.2)

    def zrobcos6(self):
        c = wmi.WMI()
        for process in c.Win32_Process():
            print(process.ProcessId, process.Name)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())




