import sys
from functions import AttributesList

## let client choose attributes and output its contents as a list
# @param    attribArg
#           arg, a list contain text name of attributions
# @return   attrs
#           a list of number represent attributes
def getAttributesList(*attribArg):
    attrs = []
    i = 1

    print("Please choose what attribute you want to scrape.", end = "")
    print(" Enter by numbers, without blank space in between.\n")
    for attrib in attribArg[0]:
        print(i, ". ", attrib)
        i = i + 1
    i = 1
    print("8 .  ALL of above\n")
    print("Please enter your choice: ", end = "")
    userInput = input()
    num = int(userInput)
    if num > 8:
        while num > 0:
            choice = num % 10
            num = int(num/10)
            attrs.insert(0, choice - 1)
    elif num == 8:
        while i <= 8:
            attrs.append(i - 1)
            i = i + 1
    else:
        attrs.append(num - 1)
    return attrs

## transfer number of attributes to text
# @param    attribsNum
#           arg, a list contain numbers that represent attributes
# @return   attribText
#           a lsit of atrribs
def getAttribInText(*attribsNum):
    attribText = []
    attribsMap = {}
    i = 0
    
    for attrib in AttributesList.attribs:
        attribsMap[i] = attrib
        i = i + 1
    for num in attribsNum[0]:
        # The 'break' is for option 8 (all above), so we don't have incorrect index after 6
        if num > 6:
            break
        attribText.append(attribsMap[num])        
    print("Transfer your attributes choice to text success.")
    return attribText

## get value of each attribute
# @param    openedPdf
#           a pdf file opened by pdf reader
# @param    *attribsNum
#           arg, a list contain numbers that represent attributes
# @return   data
#           a list of metadata
def getAttribValue(openedPdf, *attribsName):
    rawData = {}
    data = []

    rawData["page number"] = str(openedPdf.getNumPages())
    pdfInfo = openedPdf.getDocumentInfo()
    if (pdfInfo != None):
        rawData["author"] = str(pdfInfo.author)
        rawData["creator"] = str(pdfInfo.creator)
        rawData["producer"] = str(pdfInfo.producer)
        rawData["title"] = str(pdfInfo.title)
        rawData["subject"] = str(pdfInfo.subject)
        rawData["content"] = getPdfContent(openedPdf)
        for attrib in attribsName[0]:
            data.append(rawData[attrib])
        print("Scrape attribute tag success.")
    else:
        print("Couldn't find anything relate to the tag...")
        print("Press any key to exit.")
        key = input()
        sys.exit()
    return data

## get pdf page info, include page number and content of whole pdf
# @param    openedPDF
#           a pdf file opened by pdf reader
# @param    dataList
#           a list store all stripped data
# @update   dataList
#           add content in it
def getPdfContent(openedPdf):
    pdfContent = ""
    num = 0
    
    pageNum = openedPdf.getNumPages()
    while num < pageNum:
        pageInfo = openedPdf.getPage(num)
        pdfContent += pageInfo.extractText()
        num = num + 1
    return pdfContent
   

## get Xmp file info from pdf file
def getXmpValue(xmpMetaData):
    print("dc_contributor: ", xmpMetaData.dc_contributor)
    print("dc_date: ", xmpMetaData.dc_date)
    print("dc_language: ", xmpMetaData.dc_language)
    print("dc_title: ", xmpMetaData.dc_title)
    print("dc_description: ", xmpMetaData.dc_description)
