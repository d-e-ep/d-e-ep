import smtplib

##server = smtplib.SMTP_SSL("smtp.gmail.com",465)
##server.login("sample@gmail.com","password")
##server.sendmail("example@gmail.com",
##                "contact@gmail.com"
##                "hello,how are you")
##
##server.quit()

#project-->

##import stdiomask
##password1 = stdiomask.getpass()
##print(password1)
##sender_email =  "deep1997000@gmail.com"
##receiver_email =  "deepakip82@gmail.com"
##password = input(str("please enter your password:"))
##messeage = "work is done"
##
##server = smtplib.SMTP("smtp.gmail.com",587)
##server.starttls()
##server.login(sender_email,password)
##print("login success")
##server.sendmail(sender_email , receiver_email,"you'll be successfull")
##print("email has been sent to",receiver_email)






import csv 

import os
from pytube import YouTube
with open(r'C:\Users\Deepak\Desktop\Dwnld.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[2])
        print(type(row[2]))
        if row[2].strip() !="urls":
            youtube_link = row[2]
            YouTube(youtube_link).streams.first().download()
            msg = EmailMessage()
            msg['Subject']="video download result"
            msg['From']= "deepakip82@gmail.com"
            msg['To']=row[1]
            msg.set_content(" video successfully downloaded ")
            mail_id=r"deepakip82@2gmail.com"
            password = r"kapeed111"
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
                server.login(mail_id,password)
                server.send_message(msg)














