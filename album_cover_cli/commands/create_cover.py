from PIL import Image, ImageFont
from slugify import slugify

from utils.text_handler import TextHandler
from utils.image_handler import ImageHandler

def create_cover(args):
  txt_handler = TextHandler()
  img_handler = ImageHandler()

  image_path = args.image_path
  image = Image.open(image_path)
  cover_height = 1024
  cropped_image = img_handler.resize_and_crop_image(image, cover_height)

  blend = Image.open('images/filter.png')
  cover = img_handler.overlap_images(cropped_image, blend)

  font_title = ImageFont.truetype('fonts/Poppins-Bold.ttf', size=128)
  lines = txt_handler.text_lines(args.title, font_title, 512)
  position = (1088 - 96, 96)
  img_handler.draw_text_lines(cover, font_title, lines, position, "ra")

  cover = cover.rotate(-90, expand=True)

  font_subtitle = ImageFont.truetype('fonts/SourceCodePro-SemiBold.ttf', size=64)
  lines = txt_handler.text_lines(args.subtitle, font_subtitle, 360)
  position = (96, 96)
  img_handler.draw_text_lines(cover, font_subtitle, lines, position, "la")

  font_description = ImageFont.truetype('fonts/AnonymousPro-Bold.ttf', size=48)
  lines = txt_handler.text_lines(args.description, font_description, 504)
  position = (488, 96)

  img_handler.draw_text_lines(cover, font_description, lines, position, "la")

  cover = cover.rotate(90, expand=True)

  file_name = slugify(args.title) + '.png'

  cover.save('images/covers/{}'.format(file_name))
