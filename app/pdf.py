import glob
import os
from datetime import datetime

from PIL import Image


def get_pdf(chat_id: int) -> str:
    destination_file = os.getcwd() + f"/static/images/{chat_id}/{chat_id}-{time_for_image}-{photo.file_unique_id}.jpg"

    images = glob.glob(os.getcwd() + f'/static/images/{chat_id}/*.jpg')
    if not images:
        return "There're no pictures to convert"

    image_list = []
    for image in images:
        img = Image.open(image).convert('RGB')
        image_list.append(img)
        os.remove(image)

    time_for_pdf = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    pdf_path = os.getcwd() + f'/static/pdf/{chat_id}-{time_for_pdf}.pdf'
    image_list[0].save(pdf_path, save_all=True,
                       append_images=image_list[1:])
    return pdf_path
