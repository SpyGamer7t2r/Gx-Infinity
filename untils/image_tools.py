from PIL import Image
import requests
from io import BytesIO
import os

def download_image(url: str, save_as: str = "temp.jpg") -> str:
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image.save(save_as)
        return save_as
    except Exception as e:
        return str(e)

def resize_image(path: str, max_size=(512, 512)) -> str:
    try:
        img = Image.open(path)
        img.thumbnail(max_size)
        img.save(path)
        return path
    except Exception as e:
        return str(e)

def convert_image_to_format(path: str, new_format: str = "PNG") -> str:
    try:
        base = os.path.splitext(path)[0]
        new_path = f"{base}.{new_format.lower()}"
        img = Image.open(path)
        img.save(new_path, format=new_format.upper())
        return new_path
    except Exception as e:
        return str(e)
