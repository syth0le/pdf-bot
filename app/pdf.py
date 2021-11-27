import glob
import os

from fpdf import FPDF


def pdf_main() -> str:
    pdf = FPDF()
    pdf.set_auto_page_break(0)

    imagelist = glob.glob('/coding/pdf-bot/static/images/*.jpg')
    if not imagelist:
        return "There're no pictures to convert"

    for image in imagelist:
        pdf.add_page()
        pdf.image(image, w=190, h=280)
        os.remove(image)
    pdf.output("/coding/pdf-bot/static/pdf/yourfile.pdf", "F")
    return "/coding/pdf-bot/static/pdf/yourfile.pdf"
