from google_images_download import google_images_download
from PIL import Image, ImageDraw, ImageFont
import wikiquote
import random
import textwrap


def get_quote(name):
    persons = wikiquote.search(name)
    random_quote = random.choice(wikiquote.quotes(persons[0]))
    first_sentence = random_quote.split(". ")[0]
    return first_sentence


def search(query, limit):
    try:
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords":query, "limit":limit, "print_urls":True}
        paths = response.download(arguments)
        return paths
    except 'Downloading error':
        search(query, limit)


def generate_picture_with_text(name, text, path):
    lines = textwrap.wrap(text, width=25)

    lines_height = len(lines) * 50
    basewidth = 500
    image = Image.open(path).convert('RGB')

    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Impact.ttf', size=45)
    (x, y) = (40, image.size[1] - lines_height)
    color = 'rgb(255, 255, 255)'

    y_text = y
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x, y_text), line, fill=color, font=font, align="center")
        y_text += height
    image.save(name + '.png')


def merge_images_vertically(first_image, second_image, name):
    images_list = [first_image, second_image]
    imgs = [Image.open(i) for i in images_list]

    min_img_width = min(i.width for i in imgs)
    draw = ImageDraw.Draw(imgs[0])
    font = ImageFont.truetype('Impact.ttf', size=25)
    color = 'rgb(0, 0, 0)'
    draw.text((50, 150), name + ':', fill=color, font=font, align="center")

    total_height = 0
    for i, img in enumerate(imgs):
        if img.width > min_img_width:
            imgs[i] = img.resize((min_img_width, int(img.height / img.width * min_img_width)), Image.ANTIALIAS)
        total_height += imgs[i].height

    img_merge = Image.new('RGB', (min_img_width, total_height))
    y = 0
    for img in imgs:
        img_merge.paste(img, (0, y))

        y += img.height
    img_merge.save(name + 'merged.png')


name = 'Napoleon'
paths = search(name, 1)
path = paths[0][name][0]
generate_picture_with_text(name, get_quote(name), path)
merge_images_vertically('templates\\no_one_template.png', name + ".png", name)