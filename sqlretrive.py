import mysql.connector
from openpyxl import Workbook
import os
import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets


conn = mysql.connector.connect(host = 'localhost',username='root',password='1234', database = 'face')


def start():
    print(conn)
    print("Checking for exsting log file............")
    if os.path.exists("log1.xlsx"):
        print("Removing exsting file....")
        os.remove("log1.xlsx")
        print("Removed file.......")

    my_cursor = conn.cursor()
    query2 = "SELECT * FROM student"
    my_cursor.execute(query2)

    wb = Workbook(write_only=True)
    log_ws = wb.create_sheet("demo")
        # write header
    log_ws.append(["Name","ID","TIME"])

    #for row in my_cursor:
        #print(row)

    print("..........log..........")
    for row1 in my_cursor:
            print(row1)
            name_ = row1[1]
            ID_ = row1[0]
            time = row1[2]
            log_ws.append([name_,ID_,time])

    wb.save("log1.xlsx")
        
    conn.commit()
    conn.close()

start()

def log(): 
    print("opening file")
    os.system('log1.xlsx')
    
  
    
    return

def train():
    os.system("python face-train.py")




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 50, 181, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 100, 231, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(log)#.................................................
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 180, 231, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(train)#.............................................
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 240, 201, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 20, 281, 31))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Admin Login</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Show Log file"))
        self.pushButton_2.setText(_translate("MainWindow", " Start Traning "))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">A product by The Occults</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Live Face Recgonation System</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
