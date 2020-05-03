import os

## get number of pdf files under directory and fill a list that contains all xml file names
# @param    pdfList
#           a list contain xml file names 
# @return   pdfCounter
#           how many xml file in this directory
# @update   pdfList

def countPDF(pdfList):
    currentDir = ""
    pdfCounter = 0
    fileList = []
    
    currentDir = os.getcwd()
    fileList = os.listdir()
    print("\nCurrent Directory: ", currentDir, "\n")
    print("Files under this directory: ")
    for file in fileList:
        print(file)
        if(".pdf" in file):
            pdfCounter += 1
            pdfList.append(file)
    print("\n\nTotal number of file: ", len(fileList), end = "")
    return pdfCounter
