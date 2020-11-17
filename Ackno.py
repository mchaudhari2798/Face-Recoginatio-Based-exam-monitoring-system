import mysql.connector
from selenium import webdriver


conn = mysql.connector.connect(host = 'localhost',username='root',password='1234', database = 'face')
print(conn)

print("Scan QR CODE")
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
driver.maximize_window()

def wp(Aname,Aid,Atime,i):
    j = i
    k = 0
    while(k<=j):
        name = Aname[int(k)]
        id = Aid[int(k)]
        time = Atime[int(k)]
        k = k+1
        msg = ("Hey " + name + "\n Your registration is successful  "+"\n login time: "+ time )
        count = 1
        #driver.minimize_window()
    

        user =driver.find_element_by_xpath("//span[@title='{}']".format(name))
        user.click()

        msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

        for index in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
            button.click()


print("DONE")
ch = "\0"



input("Press Enter after QR code Scaning is done ")

my_cursor = conn.cursor()
query2 = "SELECT * FROM student"
my_cursor.execute(query2)

Aname = [ ]
Aid = [ ]
Atime = [ ]
i = 0
for row1 in my_cursor:
        print(row1)
        Aname.append(row1[1])
        Aid.append(row1[0])
        Atime.append(row1[2])
        i = i + 1

#print(Aname[1] , Aid[1] , Atime[1])
wp(Aname,Aid,Atime,i)
print("________________done_____________________")








