from io import BytesIO
from PIL import Image


def resize_image(image, width, height, keep_aspect_ratio):
    if keep_aspect_ratio:
        image.thumbnail((width, height))
    else:
        image = image.resize((width, height))
    return image


def convert_image_type(image, output_format):
    # استانداردسازی فرمت
    output_format = output_format.upper()

    # رفع خطای RGBA → JPEG
    if output_format == "JPEG" and image.mode == "RGBA":
        image = image.convert("RGB")

    # تبدیل به بایت و سپس به تصویر جدید
    buffer = BytesIO()
    image.save(buffer, format=output_format)
    buffer.seek(0)

    # باز کردن تصویر از حافظه برای بازگشت به Streamlit
    converted_image = Image.open(buffer)
    return converted_image
