from functions import CountPDF

## read all xml from current directory and report result
# @return   xmlList
#           a list contain all xml files need to be processed
def readPDF():
    pdfList = []
    pdfCounter = 0
    
    count = CountPDF.countPDF(pdfList)
    print("    Total number of PDF file: ", count, "\n")

    return pdfList
