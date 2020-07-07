from sys import *
import os
import hashlib
import datetime
def hashfile(path,blocksize=1024):
    fd = open(path,"rb")
    hasher = hashlib.md5()
    buf = fd.read(blocksize)


    while(len(buf)>0):
      hasher.update(buf)
      buf = fd.read(blocksize)
    fd.close()

    return hasher.hexdigest()
def Findduplicate(path):


    exists = os.path.isdir ( path )

    dup={}

    if exists:
        for dirname , sub,file in os.walk(path):
            for file in file:
                path = os.path.join(dirname,file)
                file_hash = hashfile(path)
                if file_hash in dup:
                    dup[file_hash].append(path)
                else:
                    dup[file_hash] = [path]
        return dup
    else:
        print("invalied path")
def printduplicate(dict1):


    copy= []
    result = list(filter(lambda x : len(x)>1,dict1.values()))



    if len(result)>0:

        print("duplicate file")
        print("the following file are identical")

        icnt =0
        for result in result:
            for sub in result:
                icnt +=1
                if icnt >=2:
                    print('\t\t%s'%sub)
                    copy.append( sub )
                    with open ( "file2.txt", "w" ) as m:
                        m.writelines(copy)
                        m.close()










    else:
        print("no duplicate file")

def main ():
  print ( "File duplicate finder function" )

  try:
    arr={}
    arr = Findduplicate("F:\\a")
    printduplicate(arr)


  except FileExistsError as e:
    print (e )

if __name__ == "__main__":
  main()




