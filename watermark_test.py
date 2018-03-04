# Overlay function

from PyPDF2 import PdfFileWriter, PdfFileReader


def overlay(pdf, box, x, y, height, width):
    output_file = PdfFileWriter()
    input_file = PdfFileReader(pdf, "rb")
    logo = PdfFileReader(box, "rb")
  #  brand = PdfFileReader("LogoMakr.pdf", "rb")
    water = PdfFileReader("watermark.pdf", "rb")


    newfile = input_file.getPage(0)
    newpic = logo.getPage(0)
    #brander = brand.getPage(0)
    watermark = water.getPage(0)
    watermark.scaleTo(210, 110)
    newpic.scaleTo(width, height)

    #watermark.mergePage(newfile)
    #watermark.mergeTranslatedPage(newpic, x, y, expand=False)
    #newfile.mergeTranslatedPage(brander, 0, 670, expand=False)
    scale = 0.02
    newfile.mergeRotatedScaledTranslatedPage(watermark, 0, scale, 10, 10, expand=False)
    newfile.mergeTranslatedPage(newpic, x, y, expand=False)

    output_file.addPage(watermark)

    outputStream = (open("resume_unbiased.pdf", "wb"))
    output_file.write(outputStream)
    outputStream.close()

original = "sample_resumes/sample2.pdf"
red = "bigredbox.pdf"

# MAX COORDINATES   x_cord, y_cord = 575, 780
x_cord, y_cord = 245, 710
w, h = 126, 21

overlay(original, red, x_cord, y_cord, h, w)

# original = "test.pdf"
# red = "bigredbox.pdf"
#
# # MAX COORDINATES   x_cord, y_cord = 575, 780
# x_cord, y_cord = 245, 710
# w, h = 126, 21
#
# overlay(original, red, x_cord, y_cord, h, w)
