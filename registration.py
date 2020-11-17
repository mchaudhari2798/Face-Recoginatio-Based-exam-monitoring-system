import mysql.connector
from Acknoemail import Email1
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random as r
import os
import mysql.connector
from datetime import datetime




conn = mysql.connector.connect(host = 'localhost', username ='root',password = '1234' , database = 'face')
print(conn)
my_cursor = conn.cursor()




otpf = ""
otp = "1"
email =""
uname = ""

class Ui_MainWindow(object):
    def database(self):


        otpv = str(self.lineEdit_6.text()) 
        global otpf
        if(otp==otpv):
            otpf = 1
            print("Right otp")
        else:
            otpf = 0
            print("Wrong otp")

        if (otpf==1):
            fname = str(self.lineEdit.text())
            lname = str(self.lineEdit_2.text())
            email = str(self.lineEdit_3.text())
            password = str(self.lineEdit_4.text())
            mobile = str(self.lineEdit_5.text())

            print(fname,lname,email,password,mobile)
            today = datetime.now()
            global uname
            uname = fname+lname

            Sub = "Live Face Recgonatio System User ID"
            str1 = " \n For any information or quryes reply on this email \n Thanks & Regards \n Team The Occults "
            notice = "\n\nThe information contained in this e-mail message and/or attachments to it may contain confidential or privileged information. If you are not the intended recipient, any dissemination, use, review, distribution, printing or copying of the information contained in this e-mail message and/or attachments to it are strictly prohibited. If you have received this communication in error, please notify us by reply e-mail or telephone and immediately and permanently delete the message and any attachments. Thank you"
            msg = " Hey "+ fname+" "+lname+"\n"+" Your Registration on Live Face Recgonation System has been succesfuly completed \n Your Login Name will be :-"+uname+"\n\n"+str1+notice
            Email1.Callemail(0,email,msg,Sub)
            print("Database started")
            values =(uname,fname,lname,email,password,mobile,today)
            query1 = "INSERT INTO login(uname,fname,lname,email,password,mobileno,time) VALUES (%s , %s , %s, %s ,%s,%s,%s)"
            my_cursor.execute(query1, values)
            conn.commit()
            print("Welcome",fname,"Your ID:-",uname)
            sys.exit()
    




        else:
            email = str(self.lineEdit_3.text())
            os.system("python otperror.py "+email)
            
            print("You enter wrong OTP")

        





    def emailotp(self):
        inp = str(self.lineEdit_3.text())
        name = str(self.lineEdit.text())
        lname = str(self.lineEdit_2.text())
        
        global otp
        for i in range(4):
            otp = otp + str(r.randint(1,9))
            
        msg = "Welcome "+name+"\t"+lname+"\n Your OTP is "+otp
        Sub = "Verifaction For Live Face Recgonation System"
        Email1.Callemail(0,inp,msg,Sub)
        
        

       

        return


    def image(self):
        fname = str(self.lineEdit.text())
        lname = str(self.lineEdit_2.text())
        email = str(self.lineEdit_3.text())
        password = str(self.lineEdit_4.text())
        mobile = str(self.lineEdit_5.text())
        uname = fname[0]+lname[0]+mobile[3]+mobile[1]+mobile[3]+mobile[4]
        print("OpenCV will be started")
        os.system("python image1.py "+uname)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 291, 61))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 91, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 60, 81, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(316, 63, 61, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 140, 261, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 190, 211, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 81, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 240, 161, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 240, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 201, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 350, 301, 21))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.emailotp)#.........................................OTP
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(540, 140, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(540, 110, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 0, 441, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(470, 410, 261, 21))
        self.label_12.setObjectName("label_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 300, 151, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.image)#.......................................opencv
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 380, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.database)#.................................sign up
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#5555ff;\">Registration</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Enter your Named"))
        self.label_3.setText(_translate("MainWindow", "Enter your Email"))
        self.label_4.setText(_translate("MainWindow", "Frist name "))
        self.label_5.setText(_translate("MainWindow", "Last name"))
        self.label_6.setText(_translate("MainWindow", "Set password"))
        self.label_7.setText(_translate("MainWindow", "Enter your Mobile no"))
        self.label_8.setText(_translate("MainWindow", "press start for Face Registration"))
        self.label_9.setText(_translate("MainWindow", "After Sign up Your Login ID will send to your whatsapp/Email "))
        self.pushButton.setText(_translate("MainWindow", "send OTP"))
        self.label_10.setText(_translate("MainWindow", "Enter OTP"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Live Face Recgonation System</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">A Product By The Occults</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "start"))
        self.pushButton_3.setText(_translate("MainWindow", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




