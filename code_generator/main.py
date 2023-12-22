import qrcode
from PIL import Image, ImageDraw, ImageFont

IMAGE_FORMAT = "PNG"
BASE_URL = "https://abdullatifghajar.github.io/weihnachtsgeschenk2023/"


def generate_qr_code(content):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img


def add_text_to_qr_image(text_under_qr, qr_img):
    qr_width, qr_height = qr_img.size
    image_width = qr_width
    text_height = 30
    image_height = qr_height + text_height

    combined_image = Image.new("RGB", (image_width, image_height), "white")
    combined_image.paste(qr_img, (0, text_height))
    draw = ImageDraw.Draw(combined_image)

    text_x = 40
    text_y = 0
    font_size = 40
    font = ImageFont.load_default(size=font_size)
    draw.text((text_x, text_y), text_under_qr, fill="black", font=font, align="center")

    return combined_image


def save_to_file(format, image, name):
    output_filename = f"{name}.{format.lower()}"
    image.save(f"output/{output_filename}")


answer_to_image = {"Thiais": "erster-test"}

if __name__ == "__main__":
    for answer, image in answer_to_image.items():
        qr_image = generate_qr_code(BASE_URL + image)
        final_image = add_text_to_qr_image(answer, qr_image)
        save_to_file(IMAGE_FORMAT, final_image, name=answer)
