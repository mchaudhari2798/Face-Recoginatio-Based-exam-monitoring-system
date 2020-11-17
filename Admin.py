import mysql.connector
from FaceTrain import facetrain

conn = mysql.connector.connect(host = 'localhost',username='root',password='1234', database = 'face')

print(conn)



#def registraion():


p =  facetrain.traning(0)

print(type(p))



