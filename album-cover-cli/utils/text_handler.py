import textwrap

class TextHandler:
  def text_lines(self, text, font, text_max_width):
    max_chars_per_line = 0

    for i in range(len(text)):
      width = font.getsize(text[:i])[0]
      if width > text_max_width:
          break
      max_chars_per_line = i

    lines = textwrap.wrap(text, width=max_chars_per_line, break_long_words=False)

    return lines
