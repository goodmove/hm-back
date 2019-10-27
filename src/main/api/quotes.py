from google_images_download import google_images_download
from PIL import Image, ImageDraw, ImageFont
import wikiquote
import random
import textwrap
import numpy as np
import cv2
import os.path as pathutils
import uuid

def get_quote(name):
    persons = wikiquote.search(name)
    random_quote = random.choice(wikiquote.quotes(persons[0]))
    return random_quote


def search(query, limit):
    try:
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords":query, "limit":limit, "print_urls":True}
        return response.download(arguments)
    except Exception as e:
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
    font = ImageFont.truetype('impact.ttf', size=45)
    (x, y) = (35, image.size[1] - lines_height-60)
    color = 'rgb(255, 255, 255)'

    y_text = y
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x, y_text), line, fill=color, font=font, align="center")
        y_text += height
    image.save(name + '.png')


# noinspection PyPackageRequirements
def merge_images_vertically(first_image, second_image, name):
    images_list = [first_image, second_image]

    imgs = [cv2.imread(i) for i in images_list]

    min_img_width = min(i.shape[1] for i in imgs)
    print(min_img_width, imgs[0].shape, imgs[1].shape)
    
    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(imgs[0], name + ':', (50, 180), font, 1.1, (0, 0, 0), 1)

    total_height = 0
    for i, img in enumerate(imgs):
        if img.shape[1] > min_img_width:
            imgs[i] = cv2.resize(img,(min_img_width, int(img.shape[0] / img.shape[1] * min_img_width)))
        total_height += imgs[i].shape[0]
    print(min_img_width, imgs[0].shape, imgs[1].shape)
    merged = np.concatenate((imgs[0], imgs[1]), axis=0)

    cv2.imwrite(name + 'merged.png', merged)
    return 0

def get_quoted_meme(name):
    paths = search(name, 5)
    final_url = None
    for index, path in enumerate(paths[0][name]):
        #try:
        generate_picture_with_text(name, get_quote(name).split(". ")[0], path)
        picture_path =  pathutils.join('pictures', name + ".png")
        merge_images_vertically(pathutils.join('templates', 'no_one_template.png'), picture_path, name)
        final_url = picture_path
        break
        #except Exception as e:
        #    print(e)

    return final_url
