# Overlay function

from PyPDF2 import PdfFileWriter, PdfFileReader


def overlay(pdf, box, x, y, height, width):
    output_file = PdfFileWriter()
    input_file = PdfFileReader(pdf, "rb")
    logo = PdfFileReader(box, "rb")

    # add page 1 from input1 to output document, unchanged
    scale = 1

    newfile = input_file.getPage(0)
    newpic = logo.getPage(0)
    newpic.scaleTo(width, height)

    #newfile.mergeRotatedScaledTranslatedPage(newpic, 0, scale, x, y, expand=False)
    newfile.mergeTranslatedPage(newpic, x, y, expand=False)

    output_file.addPage(newfile)

    outputStream = (open("resume_unbiased.pdf", "wb"))
    output_file.write(outputStream)
    outputStream.close()


# original = "test.pdf"
# red = "bigredbox.pdf"
#
# # MAX COORDINATES   x_cord, y_cord = 575, 780
# x_cord, y_cord = 245, 710
# w, h = 126, 21
#
# overlay(original, red, x_cord, y_cord, h, w)
