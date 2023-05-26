import fpdf

pdf = fpdf.FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Arial", "B", 20)
pdf.cell(160, 25, "Hancock County Boundary", border=0, align="C")
pdf.image("hancock.png", 25, 50, 110, 160)
pdf.output("map.pdf", "F")
