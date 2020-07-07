import datetime
import time
import schedule
import os
import subprocess
import psutil
#this is use to find particular task from the process and shuting down it and reopen it

def task ():
    print ( "current time is" )
    print ( datetime.datetime.now () )
    os.startfile ( "C:\WINDOWS\system32\\notepad.exe " )


def kill ():
    print ( "kiilling start" )
    for proc in psutil.process_iter ():
        # check whether the process name matches
        # print(proc.name())
        if any ( procstr in proc.name () for procstr in \
                 ["notepad"] ):
            print ( f'Killing {proc.name ()}' )
            print ( proc.name )
            proc.kill ()


def main ():
    print ( "main" )
    print ( datetime.datetime.now () )

    schedule.every ().day.at ( "21:09:00" ).do ( task )
    schedule.every ().day.at ( "21:11:00" ).do ( kill )
    schedule.every ().day.at ( "21:12:00" ).do ( task )
    schedule.every ().day.at ( "21:13:00" ).do ( kill )
    while True:
        schedule.run_pending ()
        time.sleep ( 0 )


if __name__ == "__main__":
    main ()
