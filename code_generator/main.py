import qrcode
from PIL import Image, ImageDraw, ImageFont
import random
import string

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
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', size=font_size)
    draw.text((text_x, text_y), text_under_qr, fill="black", font=font, align="center")

    return combined_image


def save_to_file(format, image, name):
    output_filename = f"{name}.{format.lower()}"
    image.save(f"output/{output_filename}")


answer_to_image = {
    "Thiais": "erster-test",
    "Lumière": "geschenk",
    "Café Gourmand": "geschenk",
    "Nice": "geschenk",
    "Literatur": "geschenk",
    "Paris du Nord": "foehn",
    "Tour de France": "restaurant",
}

wrong_answers = [
    "Paris",
    "Marseille",
    "Bordeaux",
    "Lyon",
    "Nantes",
    "Toulouse",
    "Strasbourg",
    "Montpellier",
    "Brest",
    "Nizza",
    "Rennes",
    "Lille",
    "Monaco",
    "Biarritz",
    "Cannes",
    "Saint-Tropez",
    "Saint-Malo",
    "Le Havre",
    "Reims",

    "Macron",
    "Lemire",
    "Le Pen",
    "Mélenchon",
    "Bayrou",
    "Hidalgo",
    "Bertrand",
    "Pécresse",
    "Dupond-Moretti",
    "Castex",
    "Darmanin",
    "Véran",
    "Schiappa",
    "Attal",
    "Le Maire",
    "Bachelot",
    "Dupond",
    "Dupont",
    "Dupont-Aignan",

    "Café au lait",
    "Café crème",
    "Café long",
    "Merveilleux",
    "Cougnou",
    "Boulette de Berlin",
    "Cannellés",
    "Baba au rhum",
    "Tarte Tatin",
    "Tarte aux fraises",
    "Tarte au citron",
    "Tarte aux pommes",
    "Tarte aux noix",
    "Tarte aux poires",
    "Tarte aux abricots",
    "Fromage blanc",
    "Mousse au chocolat",
    "Mousse au citron",
    "Tacos",
    "Crêpes",
    "Croissants",
    "Baguette",
    "Pain au chocolat",
    "Pain aux raisins",
    "Pain aux amandes",
    "Tradition",
    "Brioche",

    "Literatur",
    "Kunst",
    "Musik",
    "Mathematik",
    "Physik",
    "Chemie",
    "Biologie",
    "Informatik",
    "Medizin",
    "Philosophie",
    "Psychologie",
    "Theologie",
    "Geschichte",
    "Geographie",
    "Politikwissenschaften",
    "Soziologie",
    "Rechtswissenschaften",
    "Sportwissenschaften",
    "Pädagogik",

    "Fête de Bayonne",
    "Fête de la musique",
    "Fête de Cannes",
    "Noël",
    "Nouvel An",
    "Fête des Rois",
]

if __name__ == "__main__":
    for answer, image in answer_to_image.items():
        qr_image = generate_qr_code(f"{BASE_URL}?image={image}")
        final_image = add_text_to_qr_image(answer, qr_image)
        save_to_file(IMAGE_FORMAT, final_image, name=answer)

    for answer in wrong_answers:
        random_string = ''.join(random.choices(string.ascii_letters, k=4))
        qr_image = generate_qr_code(f"{BASE_URL}?r={random_string}")
        final_image = add_text_to_qr_image(answer, qr_image)
        save_to_file(IMAGE_FORMAT, final_image, name=answer)