from PyPDF2 import PdfFileWriter, PdfFileReader

# 开始页
start_page = 1

# 截止页
end_page = 5

output = PdfFileWriter()
pdf_file = PdfFileReader(open("input.pdf", "rb"))
pdf_pages_len = pdf_file.getNumPages()

# 保存input.pdf中的1-5页到output.pdf
for i in range(start_page-1, end_page):
    output.addPage(pdf_file.getPage(i))

outputStream = open("output.pdf", "wb")#pdf文件的的读入方式必须是二进制格式的
output.write(outputStream)
outputStream.close()