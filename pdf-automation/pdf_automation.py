import PyPDF2
from fpdf import FPDF

# Opening and extracting text from local pdf file
#file = open('yourfile.pdf', 'rb')
#reader = PyPDF2.PdfFileReader(file)
#activePage = reader.getPage(0)
#print(activePage.extract_text())

# Creating a PDF file - Automated & Designed for repetitive generation

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('pdf_icon.png', 165, 15, 33)
        # Helvetica 12
        self.set_font('helvetica', 'C', 12)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Example', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5cm from bottom
        self.set_y(-15)
        # helvetica italic 8
        self.set_font('helvetica', 'I', 8)
        # Page Number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


# Instatiation of classes
pdf = FPDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Arial', '', 12)
for i in range(1, 10):
    pdf.cell(0, 10, 'Example line: ' + str(i), 0, 1)
pdf.output('pdf-automation/data', 'F')