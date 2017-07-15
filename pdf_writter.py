from PyPDF2 import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import math
packet = StringIO.StringIO()
can = canvas.Canvas(packet, pagesize=letter)
#########App Number#######################
can.setFont('Helvetica-Bold', 10)
x = 90
y = 529
can.drawString(x,y,'AMIT KUMAR GUPTA')
can.setFont('Helvetica-Bold', 10)
x = 110
y = 503
can.drawString(x,y,'2016')
can.setFont('Helvetica-Bold', 10)
x = 370
y = 503
can.drawString(x,y,'B.Tech' + '(Electrical)')
can.setFont('Helvetica-Bold', 10)
x = 135
y = 477
can.drawString(x,y,'5/4B/1 Daud Nagar, Naini, Allahabad - 211008')
can.setFont('Helvetica-Bold', 10)
x = 135
y = 409
can.drawString(x,y,'#361, Ground Floor, ST Bed Layout, Koramongala, Bengaluru, Karanataka - 560034')
can.setFont('Helvetica-Bold', 10)
x = 115
y = 356
can.drawString(x,y,'amit@availfinance.in(ofc) / hriks@outlook.com ')
can.setFont('Helvetica-Bold', 10)
x = 105
y = 330
can.drawString(x,y,'+91-XXXXXXXXXX')
can.setFont('Helvetica-Bold', 10)
x = 325
y = 302
can.drawString(x,y,'Avail Finance, ANI, 3rd and 4th Floor,')
can.setFont('Helvetica-Bold', 10)
x = 30
y = 275
can.drawString(x,y,'Ezone Kormangala, Bengaluru, Karanataka')
can.setFont('Helvetica-Bold', 10)
x = 100
y = 248
can.drawString(x,y,'Software Developer')
can.setFont('Helvetica-Bold', 10)
x = 320
y = 248
can.drawString(x,y,'Bengaluru')
can.setFont('Helvetica-Bold', 10)
x = 490
y = 248
can.drawString(x,y,'3 LPA')
can.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
  # read your existing PDF
existing_pdf = PdfFileReader(file("form.pdf", "rb"));
output = PdfFileWriter()
  # add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
over0 = new_pdf.getPage(0)
page.mergeRotatedTranslatedPage(over0,0,over0.mediaBox.getWidth() / 2,over0.mediaBox.getWidth() / 2)
packet2 = StringIO.StringIO()
can2 = canvas.Canvas(packet2, pagesize=letter)
can2.setFont('Helvetica-Bold', 10)
#############################ANNEXTURE####################################
x = 110
y = 672
can2.drawString(x,y,'name')
x= 110
y = 640
can2.drawString(x,y,'employee_code')
can2.save()
packet2.seek(0)
# packet2.seek(0)
new_pdf2 = PdfFileReader(packet2)
#page2 = existing_pdf.getPage(1)
#over2 = new_pdf2.getPage(0)
#page2.mergeRotatedTranslatedPage(over2,0,over2.mediaBox.getWidth() / 2,over2.mediaBox.getWidth() / 2)
output.addPage(page)
#output.addPage(page2)
outputStream = file("new_.pdf", "wb")
output.write(outputStream)
outputStream.close()
print new_pdf2
