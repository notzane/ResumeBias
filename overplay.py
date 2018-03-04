# Overlay function

from PyPDF2 import PdfFileWriter, PdfFileReader


def overlay(pdf, box, x, y, height, width):
    output_file = PdfFileWriter()
    input_file = PdfFileReader(pdf, "rb")
    logo = PdfFileReader(box, "rb")
    brand = PdfFileReader("LogoMakr.pdf", "rb")

    newfile = input_file.getPage(0)
    newpic = logo.getPage(0)
    brander = brand.getPage(0)
    brander.scaleTo(210, 110)
    newpic.scaleTo(width, height)

<<<<<<< HEAD
=======
    #newfile.mergeRotatedScaledTranslatedPage(newpic, 0, scale, x, y, expand=False)
>>>>>>> 12c8537c33ead8785021c977eb64f703451b3ab6
    newfile.mergeTranslatedPage(newpic, x, y, expand=False)
    newfile.mergeTranslatedPage(brander, 10, 670, expand=False)

    output_file.addPage(newfile)

    outputStream = (open("resume_unbiased.pdf", "wb"))
    output_file.write(outputStream)
    outputStream.close()


<<<<<<< HEAD
original = "resume.pdf"
red = "bigredbox.pdf"

# MAX COORDINATES   x_cord, y_cord = 575, 780
x_cord, y_cord = 245, 710
w, h = 126, 21

overlay(original, red, x_cord, y_cord, h, w)

=======
>>>>>>> 12c8537c33ead8785021c977eb64f703451b3ab6
