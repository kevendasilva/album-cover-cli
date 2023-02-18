import textwrap

def calculate_max_chars_per_line(text, font, max_width):
    max_chars = 0
    for i in range(len(text)):
        width = font.getsize(text[:i])[0]
        if width > max_width:
            return max_chars
        max_chars = i
    return max_chars

def text_lines(text, font, text_max_width):
  font_width = font.getsize(text)[0]
  max_chars_per_line = calculate_max_chars_per_line(text, font, text_max_width)
  lines = textwrap.wrap(text, width=max_chars_per_line, break_long_words=False)

  return lines
