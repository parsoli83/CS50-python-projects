from fpdf import FPDF
page=FPDF(orientation="P",format="A4")
page.add_page()
page.set_font("helvetica", "B", 60)
page.cell(txt="CS50 Shirtificate",align='C',center=True)
a4_height=297
a4_width=210
page.image('shirtificate.png', x= 10, y= 80, w=190)
page.set_text_color(255,255,255)
page.set_font("helvetica", "B", 30)
page.cell(txt=f"{input('Name: ')} took CS50",h=250,align='C',center=True)
page.output("shirtificate.pdf")
