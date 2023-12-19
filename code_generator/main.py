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
    image_height = qr_height + 30

    combined_image = Image.new("RGB", (image_width, image_height), "white")
    combined_image.paste(qr_img, (0, 0))

    draw = ImageDraw.Draw(combined_image)
    text_x = 0
    text_y = qr_height + 5  # 5 pixels padding from the QR code
    draw.text((text_x, text_y), text_under_qr, fill="black")

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
