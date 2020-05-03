import sys

## print program info
def showInfo():
    print("******************************")
    print("*    PDF Scrapper v1.0.0     *")
    print("*     Author: Zhiren Xu      *")
    print("*  published data: 4/09/20   *")
    print("******************************")

## print exit message
# @param    fileOut
#           name of output file
def sysExit(fileOut):
    print("The program is finished. \nThe output file is: ", fileOut, " .")
    print("It is located in the same folder with your main.py program. Press enter to exit.")
    key = input()
    sys.exit()
