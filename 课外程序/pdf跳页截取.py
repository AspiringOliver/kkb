import PyPDF2 as pdf

inputfile = "input.pdf"
outputfile = "output1.pdf"
reader = pdf.PdfFileReader(inputfile)
pages = [1, 3, 5, 7]
getpages = list()

for i in pages:
    page = reader.getPage(i - 1)  # page number starts with 0
    getpages.append(page)

writer = pdf.PdfFileWriter()
for page in getpages:
    writer.addPage(page)
with open(outputfile, 'ab') as fh: #pdf文件的的读入方式必须是二进制格式的
    writer.write(fh)

# outputStream = open(outputfile, "wb")
# writer.write(outputStream)
# outputStream.close()
