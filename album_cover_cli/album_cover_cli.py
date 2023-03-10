import argparse
import sys

from commands.create_cover import create_cover
from utils.image_handler import ImageHandler

class AlbumCoverCLI:
  CLI_VERSION = "Album Cover Generator - CLI"

  def __init__(self):
    self.parser = argparse.ArgumentParser(
                    prog="album-cover-cli",
                    description="Automation to create album covers",
                    epilog="Developed by: @kevendasilva",
                    usage="%(prog)s [options]"
                  )

    self.parser.version = self.CLI_VERSION
    self.parser.add_argument("-v", "--version", action="version")
    subparsers = self.parser.add_subparsers(help="valids arguments (use -h for help)", dest="command")
    self._create_cover_parser(subparsers)

    self._run()

  def _run(self):
    args = self.parser.parse_args()

    if args.command == "cover":
      create_cover(args)
    else:
      self.parser.print_help()
      sys.exit(1)

  def _create_cover_parser(self, subparsers):
    img_handler = ImageHandler()

    self.cover_parser = subparsers.add_parser("cover", help="cover -h")
    self.cover_parser.add_argument("-t", "--title", help="album name", type=str, required=True)
    self.cover_parser.add_argument("-s", "--subtitle", help="album subtitle", type=str)
    self.cover_parser.add_argument("-d", "--description", help="album description", type=str)
    self.cover_parser.add_argument("-ip", "--image-path", help="album image path", type=img_handler.check_path, required=True)
