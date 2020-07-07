import os
from sys import *
import re
def typechanger(path,ext1,ext2):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)





    if exists:
        for folder,subfolder,file in os.walk(path):
            for file in file:
                if file.endswith(ext1):
                    infilename = os.path.join ( path, file )

                    oldbase = os.path.splitext ( file )
                    newname = infilename.replace ( ext1, ext2 )
                    os.rename ( infilename, newname )

def main():
    print("File copy function")

    try:
        typechanger("F:\\a",".doc", ".txt")


        exit()
    except Exception:
        print("Error: invalied input")
if __name__=="__main__":
    main()

