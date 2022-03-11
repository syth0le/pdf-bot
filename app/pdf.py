import glob
import os

from PIL import Image


def get_pdf(chat_id: int) -> str:
    images = glob.glob(os.getcwd() + f'/static/images/{chat_id}/*.jpg')
    if not images:
        return "There're no pictures to convert"

    image_list = []
    for image in images:
        img = Image.open(image).convert('RGB')
        image_list.append(img)
        os.remove(image)

    pdf_path = os.getcwd() + f'/pdf/pdf.pdf'
    image_list[0].save(pdf_path, save_all=True,
                       append_images=image_list[1:])
    return pdf_path
