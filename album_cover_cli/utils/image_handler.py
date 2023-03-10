import argparse
from PIL import Image, ImageDraw, ImageFont

from utils.text_handler import TextHandler

class ImageHandler:
  def resize_and_crop_image(self, image, new_height):
    width, height = image.size

    new_width = int(new_height * width / height)
    resized_image = image.resize((new_width, new_height))

    resized_width, resized_height = resized_image.size

    left = (resized_width - new_height) / 2
    top = (resized_height - new_height) / 2
    right = (resized_width + new_height) / 2
    bottom = (resized_height + new_height) / 2

    return resized_image.crop((left, top, right, bottom))

  def overlap_images(self, image1, image2):
    w1, h1 = image1.size
    w2, h2 = image2.size

    x1, y1 = (w2 - w1) // 2, (h2 - h1) // 2
    x2, y2 = 0, 0

    new_img = Image.new("RGBA", (max(w1, w2), max(w1, w2)), (0, 0, 0, 0))

    new_img.paste(image1, (x1, y1))
    new_img.paste(image2, (x2, y2), image2)

    return new_img

  def draw_text_lines(self, image, font, lines, position, anchor):
    draw = ImageDraw.Draw(image)

    for line in lines:
      height = draw.textsize(line, font=font)[1]
      draw.text(position, line, font=font, fill='white', anchor=anchor)
      position = (position[0], position[1] + height)

  def draw(self, cover, texts_data, anchor="la"):
    txt_handler = TextHandler()

    for text_data in texts_data:
      text, font_file, font_size, max_width_text, position = text_data
      font = ImageFont.truetype(font_file, size=font_size)
      lines = txt_handler.text_lines(text, font, max_width_text)
      self.draw_text_lines(cover, font, lines, position, anchor)

  def check_path(self, path):
    try:
      Image.open(path)
      return path
    except IOError:
      raise argparse.ArgumentTypeError("The path '{}' is not a valid image".format(path))
