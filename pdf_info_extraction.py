"""
@author: Amirmoradi94 (GitHub)
"""

from PyPDF2 import PdfFileReader
import os

# Get a list of total pdf files
list_pdf = os.listdir("...")

# a function to extract the title of papers
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
    #author = info.author
    #creator = info.creator
    #producer = info.producer
    #subject = info.subject
    return info.title 

# The code starts from here.
if __name__ == '__main__':
    myfile = open("pdf_titles.txt","w") # create a txt file to save titles
    for pdf in list_pdf:
        try:
            path = ".../" + pdf # directory of each pdf file
            title = get_info(path) # extract the tile
            target = pdf + ": " + str(title) # example: 0223.pdf: An MPC Strategy for Low-Thrust Space Debris Rendezvous
            myfile.write("%s\n\n" % target) # save the target in each row of the ext file
        except:
            print(pdf)
    myfile.close()