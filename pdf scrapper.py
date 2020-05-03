from functions import Greeting
from functions import Attributes
from functions import ReadPDF
from functions import SimpleCSV
from functions import RunProcess
from functions import AttributesList

def main():
    attributes = []
    outFile = ""
    pdfs = []
    
    #greeting
    Greeting.showInfo()
    #get outfile name (csv)
    outFile = SimpleCSV.getCSVOutput()
    #get attribute list(csv)
    attributes = Attributes.getAttributesList(AttributesList.attribs)
    #process
    pdfs = ReadPDF.readPDF()
    RunProcess.scrapePDF(attributes, pdfs, outFile)
    #output, exit
    Greeting.sysExit(outFile)
    
if __name__ == "__main__":
    main()
