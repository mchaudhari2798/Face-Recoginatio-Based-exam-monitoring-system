import numpy as np 
import cv2
import pickle
from datetime import datetime
import mysql.connector
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

print(".................Welcom..........")



#today = datetime.now()

conn = mysql.connector.connect(host = 'localhost', username ='root',password = '1234' , database = 'face')
print(conn)
my_cursor = conn.cursor()
query1 = "INSERT INTO student1(ID,name,time,eyec,facec) VALUES (%s , %s , %s, %s, %s)"



def db(name1,id1,eye_counter,face_counter):
    print("Welcome",name1,"Your ID:-",id1)
    values =(0,name1,endTime1,eye_counter,face_counter)
    my_cursor.execute(query1, values)
    conn.commit()


face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

eye_counter = 0
face_counter = 0
name = "\0"
c = 0
flg = 0
name1 = " "
endTime1 = ''



class Ui_MainWindow(object):

    def Start(self):
        

        extime = str(self.lineEdit_3.text())
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=int(extime))

        global name1
        name1 = str(self.lineEdit.text())
        id1 = str(self.lineEdit_2.text())

        labels = {"person_name": 1}
        with open("labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}
            
        cap = cv2.VideoCapture(0)
        print("Procesing..............")
        global c
        global endTime1
        endTime1 = datetime.datetime.now() + datetime.timedelta(minutes=1)
        

        while(1):
            if datetime.datetime.now() >= endTime:
                break
            endTime1 = datetime.datetime.now() + datetime.timedelta(minutes=1)
            while(1):
                if datetime.datetime.now() >= endTime1:
                    break
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
                            face_counter += 1
                            c = face_counter

                        
                        
                        
                        
                    
                    img_item = "my-image.png"
                    cv2.imwrite(img_item, roi_colour)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    color = (255, 0, 0) #blue
                    stroke = 2
                    end_cord_x = x + w
                    end_cord_y = y + h
                    str1 = name1 + str(c) + "% Done"
                    cv2.rectangle(frame, (x, y),(end_cord_x , end_cord_y), color, stroke)
                    cv2.putText(frame, str1, (x,y), font, 1, (255,255,255), stroke, cv2.LINE_AA)

                    eyes =eye_cascade.detectMultiScale(roi_gray)
                    for(ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_colour,(ex, ey),(ex+ew, ey+eh),(0,255,0),2)
                        if (ex):
                            global eye_counter
                            #print("Eyes open")
                            eye_counter += 1
                            #print(eye_counter)


                # smile = smile_cascade.detectMultiScale(roi_gray)
            # for(sx,sy,sw,sh) in smile:
                #  cv2.rectangle(roi_colour,(sx, sy),(sx+sw, sy+sh),(0,150,0),2)

                cv2.imshow('frame',frame)
                if (cv2.waitKey(20) & 0xFF == ord('q')):
                    break
                # if(c >= int(int(extime)*60)):
                    # print("\n..........Processing Done........ ")
                    # break
                
            db(name,id,eye_counter,face_counter)


        cap.release()
        cv2.destroyAllWindows()

        print("Eye open for ")
        print(eye_counter)
        print("face live for ")
        print(face_counter)

        id2 = 000
        db(name1,id2,eye_counter,face_counter)







    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 161, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 0, 311, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 120, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 160, 91, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 120, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 160, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 210, 61, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 210, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 360, 201, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Start)#.................................................start
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Start Exam</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Live Face Recgonation System</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Enter Your Name "))
        self.label_4.setText(_translate("MainWindow", "Enter Your ID"))
        self.label_5.setText(_translate("MainWindow", "Exam Code "))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">A product By The Occults</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Start Exam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())








