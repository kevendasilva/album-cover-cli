from PIL import Image
from slugify import slugify

from utils.image_handler import ImageHandler

def create_cover(args):
  img_handler = ImageHandler()

  image_path = args.image_path
  image = Image.open(image_path)
  cover_height = 1024
  cropped_image = img_handler.resize_and_crop_image(image, cover_height)

  blend = Image.open('images/filter.png')
  cover = img_handler.overlap_images(cropped_image, blend)

  texts_data = [(args.title, 'fonts/Poppins-Bold.ttf', 128, 512, (1088 - 96, 96))]
  img_handler.draw(cover, texts_data, "ra")

  if args.subtitle or args.description:
    cover = cover.rotate(-90, expand=True)
    texts_data = []
    if args.subtitle:
      texts_data.append((args.subtitle, 'fonts/SourceCodePro-SemiBold.ttf', 64, 360, (96, 96)))
    if args.description:
      texts_data.append((args.description, 'fonts/AnonymousPro-Bold.ttf', 48, 504, (488, 96)))
    img_handler.draw(cover, texts_data)
    cover = cover.rotate(90, expand=True)

  file_name = slugify(args.title) + '.png'

  cover.save('images/covers/{}'.format(file_name))
