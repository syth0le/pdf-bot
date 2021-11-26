import glob

from PIL import Image
from fpdf import FPDF

pdf = FPDF()

im1 = Image.open("/coding/pdf-bot/static/images/1.jpg")
im2 = Image.open("/coding/pdf-bot/static/images/2.jpg")
im3 = Image.open("/coding/pdf-bot/static/images/3.jpg")
imagelist = [im2, im3]

pdf1_filename = "/coding/pdf-bot/static/pdf/bbd1.pdf"

im1.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=imagelist)

imagelist = glob.glob('static/images/*.jpg')

for image in imagelist:
    pdf.add_page()
    pdf.image(image, 10, 210, 297)
pdf.output("/coding/pdf-bot/static/pdf/yourfile.pdf", "F")
