import smtplib
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

class Email1:
  

    def Callemail(self,email,message,Sub):

        sender_email ='theoccultsfacerecognition@gmail.com'
        rec_email = email

        password = 'theoccults12'

        inp = message

        '''
        msg = MIMEMultipart()
        msg['From'] = 'Team The Occults'
        msg['To'] = 'Pratik Ingale'
        msg['Subject'] = 'Ack
        msg['Text'] = inp
        '''

        SUBJECT = Sub  
        TEXT = inp

        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)


        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(sender_email,password)
        server.ehlo()
        print('login done')

        #server.sendmail(sender_email,rec_email,msg.as_string())

        server.sendmail(sender_email,rec_email,message)
        print("Email send")