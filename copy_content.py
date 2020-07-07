import os
from  sys import *
def copies(dir,file,name):
     print(os.getcwd())
     directory= dir
     Old_file_name = file
     New_file = name
     folder = os.path.join(directory,Old_file_name)
     folder_2 = os.path.join(directory,New_file)
     with open(folder,"rb") as file1:
          with open(folder_2,"wb") as file2:
             buf = file1.read()
             buf2= file2.write(buf)
             file2.close()

def main():
    print("File copy function")
    print("Application name: "+ argv[0])
    if (len(argv)!=4):
        print("Error: invalied no of argument")
        exit()
    if (argv[1]== "-h") or (argv[1]== "H"):
        print("the script is used to transvers through specific directory")
        exit()
    if (argv[1] == "-u") or (argv[1] == "u"):
       print ( "apploication name absoulte of psth" )
       exit ()
    try:
        copies(argv[1],argv[2],argv[3])


        exit()
    except Exception:
        print("Error: invalired input")
if __name__=="__main__":
    main()
