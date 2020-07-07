import os
import schedule
import psutil
import time
import datetime
from urllib.error import URLError
import  urllib
import smtplib
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
def is_connected():
    try:

        urllib.urlopen("http://gmail.com",timeout = 1)
        return True
    except URLError as err:
        return False
def mailsender(filename,time):
  try:
    fromaddr = "sender mail id"
    toaddr = "reciver mail id"
    msg = MIMEMultipart()
    msg['from'] =fromaddr
    msg['to'] = toaddr
    body = """
    Hello %s,
    Welcome to vaibhav  infotech.
    Please find attachment wich contain log of running process.
    Log file is created at:%s
    
    Thanks &Regards;
    vaibhav misal
    """%(toaddr,time)

    subject = """
    Vaibhav infotech process log at :%s"""%(time)
    msg['subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    attachment = open(filename,"rb")
    p = MIMEBase('application','octet-stream')
    p.set_payload( attachment.read() )
    encoders.encode_base64(p)
    p.add_header('content-disposition',"attachment; filename = %s"% filename)
    msg.attach(p)
    s = smtplib.SMTP('smpt.gmail.com',587)
    s.starttls()
    s.login(fromaddr,"Insert password here")
    text= msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()
    print("log file is succesfully sent through mail")
  except Exception as E:
      print("unable to send mail",E)
def log_file(file ="log_file"):
    listprocess = []
    if not os.path.exists(file):
     try:
         os.mkdir(file)
     except Exception as E:
         print(E)
    spliter = "*"*80
    timestr = time.strftime ( "%d%m%y_%H%M%S" )
    log_path = os.path.join ( file, "marvellous_" + timestr + ".txt" )

    f = open(log_path,"w")
    f.write("\t\t%s"%spliter)
    f.write("Log file of system %s"+ time.ctime())
    f.write("\t\t%s"%spliter)





    for proc in psutil.process_iter():
     try:
         pinfo= proc.as_dict(attrs=["pid","name","username"])
         pinfo["vms"] = proc.memory_info().vms/(1024*1024)
         listprocess.append(pinfo)
     except (psutil.ZombieProcess, psutil.NoSuchProcess,psutil.AccessDenied):
         pass
    for elem in listprocess:
     f.write( "\t\n%s"%elem )
    print("the log file is created at location: %s" %(log_path))
    conected =is_connected()
    if conected:
        starttime =time.time()
        mailsender(log_path,time.ctime())
        endtime =time.time()
        print("the %s took to send mail "%(endtime-starttime))
    else:
        print("no internet connection")

def main():

    print("the process running on sstem are ")
    log_file()


main()