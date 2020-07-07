import os
from sys import *


def DisplayFiles (path, filename):
    print ( filename )
    flag = os.path.isabs ( path )

    if flag == False:
        path = os.path.abspath ( path )

    exists = os.path.isdir ( path )

    if exists:
     for folder ,subfolder,file in os.walk(path):
         for file in file:

                if file.endswith ( filename):
                    print(file)
def main():
    try:
        DisplayFiles("f:\\",".txt")


        exit()
    except Exception:
        print("Error: invalired input")
if __name__=="__main__":
    main()

