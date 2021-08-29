
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
