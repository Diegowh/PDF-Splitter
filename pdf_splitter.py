from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("pdf_prueba.pdf")
writer = PdfWriter()

# Obtiene la parte izquierda del PDF
page = reader.pages[2]
original_width = page.mediabox[2] - page.mediabox[0]
new_right = original_width / 2
page.mediabox.upper_right = (new_right, page.mediabox[3])
writer.add_page(page)

with open("PyPDF2-output.pdf", "wb") as fp:
    writer.write(fp)
    
# Obtiene la parte derecha del PDF
reader2 = PdfReader("pdf_prueba.pdf")
writer2 = PdfWriter()

page2 = reader2.pages[2]
original_width2 = page2.mediabox[2] - page2.mediabox[0]
new_left2 = original_width2 / 2
page2.mediabox.lower_left = (new_left2, page2.mediabox[1])
writer2.add_page(page2)

with open("PyPDF2-output-2.pdf", "wb") as fp2:
    writer2.write(fp2)