import glob

from PIL import Image
from fpdf import FPDF


def pdf_main():
    pdf = FPDF()
    pdf.set_auto_page_break(0)

    imagelist = glob.glob('/coding/pdf-bot/static/images/*.jpg')

    for image in imagelist:
        pdf.add_page()
        pdf.image(image, w=190, h=280)
        print(pdf)
    pdf.output("/coding/pdf-bot/static/pdf/yourfile.pdf", "F")
    return "/coding/pdf-bot/static/pdf/yourfile.pdf"


def pdf_sub():
    im1 = Image.open("/coding/pdf-bot/static/images/1.jpg")
    im2 = Image.open("/coding/pdf-bot/static/images/2.jpg")
    im3 = Image.open("/coding/pdf-bot/static/images/3.jpg")
    imagelist = [im2, im3]

    pdf1_filename = "/coding/pdf-bot/static/pdf/bbd1.pdf"

    im1.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=imagelist)
