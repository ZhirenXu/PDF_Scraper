from PyPDF2 import PdfFileReader
from functions import SimpleCSV
from functions import AttributesList
from functions import Attributes
import sys

## the main process of scrap
# @param    attribsNum
#           a list contains numbers that represent attributes
# @param    pdfList
#           a list of pdf file to process
# @param    fileOut
#           output csv file name        
def scrapePDF(attribsNum, pdfList, fileOut):
    metaData = []
    attribsInText = []
    
    csvOut = open(fileOut, "w", encoding = "utf8")
    #transfer code form of attribs into text form
    attribsInText = Attributes.getAttribInText(attribsNum)
    attribsInText.insert(0, "file name")
    SimpleCSV.writeCSV(attribsInText, csvOut)
    #delete file name because we can't find that in pdf
    attribsInText.pop(0)
    for pdf in pdfList:
        openedPDF = PdfFileReader(open(pdf, "rb"))
        #get author, creator, producer, subject, title
        # xmp data is all empty
        #xmpInfo = openedPDF.getXmpMetadata()
        #Attributes.getXmpValue(xmpInfo)
        #get a list of metadata corresponding to attribs
        metaData = Attributes.getAttribValue(openedPDF, attribsInText)
        #Attributes.getPdfContent(openedPDF, metaData)
        metaData.insert(0, str(pdf))
        SimpleCSV.writeCSV(metaData, csvOut)
    csvOut.close()
