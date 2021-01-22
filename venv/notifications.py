import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class notifications():


    def __init__(self, ipAddress, location, message):
        self.ipAddress = ipAddress
        self.location = location
        self.message = message

    def sendEmail(self):

        sender = 'davsuar@amazon.com'
        receivers = ['deltacompu2@gmail.com']

        message = """Subject: SMTP e-mail test

        
        """+"SSP printer located near pole: "+self.location+" with ip address: "+self.ipAddress+" presents the next problem: "+self.message
        try:
            smtpObj = smtplib.SMTP('smtp.amazon.com')
            smtpObj.sendmail(sender, receivers, message)
            print ("Successfully sent email")
        except SMTPException:
            print ("Error: unable to send email")
