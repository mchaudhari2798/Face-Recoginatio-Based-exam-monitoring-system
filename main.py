import os
from PyQt5 import QtCore, QtGui, QtWidgets

def realtime():
    print("Realtime is starting")
    os.system("python Realtime.py")
    print("DONE REALTIME")
    return



def sqlretrive():
    print("Starting sql ")
    os.system("python sqlretrive.py")
    print("DONE SQL")
    return
def monitraring():
    print("Starting monitarin")
    os.system("python Monitaring.py")
    return


class Ui_TheOccults(object):
    def registraion(self):
        print("Registration start")

        os.system("python registration.py")
        print("DONE TRAINING")
        return







    def setupUi(self, TheOccults):
        TheOccults.setObjectName("TheOccults")
        TheOccults.setWindowModality(QtCore.Qt.NonModal)
        TheOccults.resize(787, 557)
        TheOccults.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        TheOccults.setAutoFillBackground(True)
        TheOccults.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(TheOccults)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 0, 381, 81))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 150, 281, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.registraion)#...................................................1
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 250, 281, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(sqlretrive)#...........................................2
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 350, 321, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(realtime)#......................................3
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 350, 331, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(monitraring)#...........................................4
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 100, 311, 41))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 450, 411, 41))
        self.label_2.setObjectName("label_2")
        TheOccults.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(TheOccults)
        self.statusBar.setObjectName("statusBar")
        TheOccults.setStatusBar(self.statusBar)

        self.retranslateUi(TheOccults)
        QtCore.QMetaObject.connectSlotsByName(TheOccults)

    def retranslateUi(self, TheOccults):
        _translate = QtCore.QCoreApplication.translate
        TheOccults.setWindowTitle(_translate("TheOccults", "TheOccults"))
        self.label.setText(_translate("TheOccults", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#0e2db4;\">Welcome</span></p></body></html>"))
        self.pushButton.setText(_translate("TheOccults", "Registraion"))
        self.pushButton_2.setText(_translate("TheOccults", "Admin Login"))
        self.pushButton_3.setText(_translate("TheOccults", "Attendace"))
        self.pushButton_4.setText(_translate("TheOccults", "Strart Exam "))
        self.label_3.setText(_translate("TheOccults", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Live Face Recgonation System</span></p></body></html>"))
        self.label_2.setText(_translate("TheOccults", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">A Product By The Occults</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TheOccults = QtWidgets.QMainWindow()
    ui = Ui_TheOccults()
    ui.setupUi(TheOccults)
    TheOccults.show()
    sys.exit(app.exec_())
