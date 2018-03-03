#extract_text.py
#Zane Alpher
#3/3/18


import pdfminer.high_level #need pdfminer module 

def extract_text(file1, outfile, output_type):

    laparams = pdfminer.layout.LAParams() #from their example code

    outfp = open(outfile, "wb") #open an output file (w-write, b-binary mode)

    with open(file1, "rb") as fp: #try to open input file (r-read)
        pdfminer.high_level.extract_text_to_fp(fp, **locals())


# example uses
#    extract_text("resume.pdf", "resume.txt", "text")
#    extract_text("resume.pdf", "resume.xml", "xml")
