from sys import *
import time
import smtplib
import urllib
from urllib.error import URLError

def is_connected():
    try:
        urllib.urlopen("http:// gmail.com",timeout=1)
        return True
    except urllib.error as err:
        return False
def mailsender(gmailaccount,password):
    sent_from = gmailaccount
    to =[""] # insert reciver mail id here in between ["HERE"]
    email_text ="welcome"
    try:
        server= smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()
        server.login(gmailaccount,password)
        server.sendmail(sent_from,to,email_text)
        server.close()
        print("mail send succesfully")
    except Exception as E:
        print("unable to send mail",E)
def main():
    print("application name" +argv[0])
    x = str(input("insert password :")) # from here we take the password from user for safety reason.
    try:
        gmail_account = " "# sender mail id in between " "
        password = x
        connected = is_connected()
        if connected:
            start_time = time.time()
            mailsender(gmail_account,password)
            end_time = time.time()
            print(" took %s sec for sending mail"%(end_time-start_time))
        else:
            print("no internet connection")
    except Exception as E:
        print(E)
if __name__=="__main__":
    main()
