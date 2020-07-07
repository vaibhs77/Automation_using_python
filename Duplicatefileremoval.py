import datetime
from sys import *
import os
import hashlib
import time
def DeletFiles(dict1):
    result = list(filter(lambda x:len(x)>1,dict1.values()))
    icnt = 0
    if len(result)>0:
        for result in result:
            for sub in result:
                icnt +=1
                if icnt>+1:
                    os.remove(sub)
            icnt= 0
    else:

        print("no duplicate found")
def hashfile(path,blocksize =1024):
    afile = open(path,"rb")
    hasher = hashlib.md5()
    buf =  afile.read(blocksize)

    while len(buf )> 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()
def findDup(path):
    flag = os.path.isabs(path)
    if flag ==False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    dup = {}
    if exists:
        for f,s,f2 in os.walk(path):
            print("current folder:"+f)
            for file in f2:
                path =os.path.join(f,file)
                file_hash = hashfile(path)
                if file_hash in dup:
                    dup[file_hash].append(path)
                else:
                    dup[file_hash]=[path]
        return dup
    else:
        print("invalied path")
def printResults(dict1):
    copy = []
    path= "C:\\Users\HP\Desktop\python assignments\ku"
    if not os.path.exists ( path ):
        os.mkdir ( path );

    filename = datetime.datetime.now ()
    path = os.path.join ( path, filename.strftime ( "%d %B" ) + ".txt" )

    f= open(path,"w")


    result = list ( filter ( lambda x: len ( x ) > 1, dict1.values () ) )

    if len ( result ) > 0:
        print("The following are duplicate file")

        for result in result:
            for sub in result:
                print("\t\t%s"%sub)
                copy.append(sub)

    for item in copy:
        f.write ( '%s\n'  % item )






def main():
    print ( "File copy function" )

    try:
        arr= {}
        starttime = time.time()
        arr = findDup("F:\\a")
        printResults(arr)
        DeletFiles(arr)
        endtime = time.time()
        print("took %s second to evalute ."% (endtime-starttime))



    except Exception:
        print ( "Error: invalired input" )


if __name__ == "__main__":
    main ()

