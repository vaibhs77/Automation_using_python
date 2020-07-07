from sys import *
import os
import hashlib

def hashfile(path,blocksize = 1024):
    afile = open(path,"rb")
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
def displaychecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    if exists:
        for f,s,f2 in os.walk(path):
            print("current folder is"+f)
            for file in f2:
                path = os.path.join(f,file)
                file_hash =hashfile(path)
                print(path)
                print(file_hash)
                print("")
    else:
        print("invalied path")
def main():
    print ( "File copy function" )

    try:
        arr=[]
        arr =  displaychecksum ( "f:\\a") #enter the file or folder whosechecksum you want to find


    except Exception as E:
        print ( "Error: invalired input",E )
    except ValueError :
        print ( "Error: invalired datatype" )


if __name__ == "__main__":
    main ()

