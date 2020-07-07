import psutil
import os


def findprocessid (processName):
    list = []
    for proc in psutil.process_iter ():
        try:
            pinfo = proc.as_dict ( attrs=['pid', "name", "create_time"] )
            if processName  in pinfo['name']:
                list.append()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return list


findprocessid ( "chrome" )
