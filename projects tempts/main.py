import glob
import fpdf
import pathlib

import pandas as pn

dd = glob.glob("dd/*.txt")
pdf = fpdf.FPDF(orientation="P", format="A4", unit="mm")
print(dd)
for filepath in dd:
    with open(filepath) as file:
        content = file.readline()
    filename = pathlib.Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family="times", style="B", size=34)
    pdf.cell(w=50, h=10, txt=filename, ln=1, align="L")
    pdf.set_font(family="Times", style="B", size=17)
    pdf.multi_cell(w=0, h=10, txt=content, border=0, align="L")
    print(content)
    print(filepath)
    print(filename)
pdf.output("output.pdf")
