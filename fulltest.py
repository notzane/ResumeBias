import recognizeName
import overplay
import find_name
import extract_text

filenamepdf = "sample_resumes/sample3.pdf"
filenametxt = "resume.txt"

extract_text.extract(filenamepdf, filenametxt, "text")

name = recognizeName.recognizeName(filenametxt)
print(name)

pos_size = find_name.find_name(filenamepdf, name)

overplay.overlay(filenamepdf, "bigredbox.pdf", *pos_size)
