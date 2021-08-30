import smtplib
import stdiomask

password1 = stdiomask.getpass()
print(password1)
sender_email =  "deep1997000@gmail.com"
receiver_email =  "deepakip82@gmail.com"
password = input(str("please enter your password:"))
messeage = "work is done"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,password)
print("login success")
server.sendmail(sender_email , receiver_email,"you'll be successfull")
print("email has been sent to",receiver_email)

