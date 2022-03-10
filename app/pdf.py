import glob
import os
from datetime import datetime

from PIL import Image


def get_pdf(chat_id: int) -> str:
    images = glob.glob(f'/coding/pdf-bot/static/images/{chat_id}/*.jpg')
    if not images:
        return "There're no pictures to convert"

    image_list = []
    for image in images:
        img = Image.open(image).convert('RGB')
        image_list.append(img)
        os.remove(image)

    time_for_pdf = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    pdf_path = f'/coding/pdf-bot/static/pdf/{chat_id}-{time_for_pdf}.pdf'
    image_list[0].save(pdf_path, save_all=True,
                       append_images=image_list[1:])
    return pdf_path
