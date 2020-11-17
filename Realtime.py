import numpy as np 
import cv2
import pickle
from datetime import datetime
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

today = datetime.now()

conn = mysql.connector.connect(host = 'localhost', username ='root',password = '1234' , database = 'face')
print(conn)
my_cursor = conn.cursor()
query1 = "INSERT INTO student(ID,name,time) VALUES (%s , %s , %s)"

def db(name1,id1):
    
    values =(id1,name1,today)
    my_cursor.execute(query1, values)
    conn.commit()
    print("Welcome",name1,"Your ID:-",id1)
    exit

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

eye_counter = 0
face_counter = 0
name = "\0"
name1 = " "
id1 = " "
c1 = 0












class Ui_MainWindow(object):
    def start(self):
        global name1
        name1 = str(self.lineEdit.text())

        global id1
        id1 = self.lineEdit_2.text()
        print("-----------------------------",name1)
        labels = {"person_name": 1}
        with open("labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}
            
        cap = cv2.VideoCapture(0)
        print("Procesing..............")
        global c1

        while(1):
            ret , frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for(x , y, w, h) in faces:
                #print(x,y,w,h)
                roi_gray = gray[y:y+h, x:x+w]
                roi_colour = frame[y:y+h, x:x+w]
                #recognization
                id_ , conf = recognizer.predict(roi_gray)
                if conf >= 45 and conf <= 85 :
                    #print(id_ ,)
                    
                    #print(labels[id_])
                    name = labels[id_]
                    if(name1 == name):
                        global face_counter
                        face_counter = face_counter + 1
                        
                    
                        c1 = face_counter*4
                        
                        
                        
                        
                    
                img_item = "my-image.png"
                cv2.imwrite(img_item, roi_colour)
                font = cv2.FONT_HERSHEY_SIMPLEX
                color = (255, 0, 0) #blue
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                str1 = name1 + str(c1) + "% Done"
                cv2.rectangle(frame, (x, y),(end_cord_x , end_cord_y), color, stroke)
                cv2.putText(frame, str1, (x,y), font, 1, (255,255,255), stroke, cv2.LINE_AA)

                eyes =eye_cascade.detectMultiScale(roi_gray)
                for(ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_colour,(ex, ey),(ex+ew, ey+eh),(0,255,0),2)
                    if (ex):
                        #print("Eyes open")
                        global eye_counter
                        eye_counter += 1
                        print(eye_counter)


            # smile = smile_cascade.detectMultiScale(roi_gray)
            # for(sx,sy,sw,sh) in smile:
                #  cv2.rectangle(roi_colour,(sx, sy),(sx+sw, sy+sh),(0,150,0),2)

            cv2.imshow('frame',frame)
            if (cv2.waitKey(20) & 0xFF == ord('q')):
                break
            if(c1 >= 100):
                print("\n..........Processing Done........ ")
                break


        cap.release()
        cv2.destroyAllWindows()

        print("Eye open for ")
        print(eye_counter)
        print("face live for ")
        print(face_counter)


        db(name1,id_)

    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 171, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 110, 111, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 160, 111, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 160, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 260, 211, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 10, 241, 21))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Attendance</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Enter Your name "))
        self.label_3.setText(_translate("MainWindow", "Enter your ID"))
        self.pushButton.setText(_translate("MainWindow", "Done"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">A product By The Occults</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Live Face Recgonation System</span></p></body></html>"))
    

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())











