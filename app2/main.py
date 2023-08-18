from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.output("mypdf.pdf")
