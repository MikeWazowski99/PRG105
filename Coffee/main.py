"""
Code to edit an image
"""

from PIL import Image, ImageFont, ImageDraw

my_image = Image.open('new_york.jpg')

title_font = ImageFont.truetype('SansPro/SourceSansPro-Black.ttf', 200)

title_text = 'USA'

image_edit = ImageDraw.Draw(my_image)

image_edit.text((850, 15), title_text, (255, 46, 74), font=title_font)

my_image.save("NewYork.jpg")
