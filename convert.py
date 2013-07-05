# Usage: convert.py filename --format=roo|html

from argparse import ArgumentParser
from substitutions import build_substitutions, COLOURS
from PIL import Image

def best(substitutions,block):
  """ Return the character best suited to represent block """
  best = None
  result = None

  for output,irc_fg,irc_bg,character in substitutions:
    error = 0
    for i in xrange(4):
      for c in xrange(3):
        error += abs(block[i][c] - output[i][c])
    if best is None or error < best:
      best = error
      result = (irc_fg,irc_bg,character)

  return result

def output_html(raw):
    """ Convert raw format to html """
    result = ['''<!DOCTYPE html><html><head><meta charset="UTF-8"><style>body { line-height:12px; font-size:12px }</style></head><body>''']
    for row in raw:
        for foreground,background,data in row:
            foreground = COLOURS[foreground]
            background = COLOURS[background]
            result.append("<span style='background:rgb%s;color:rgb%s'>%s</span>" % (str(background),str(foreground),data))
        result.append("<br/>")
    result.append("</body></html>")
    print "".join(result)
            
    


if __name__ == '__main__':
    
    parser = ArgumentParser()
    parser.add_argument("filename",help="image filename, you probably want to have already sorted the palette")
    parser.add_argument("--format", action="store",
                        default="roo",help="output format, html or roo")
    args = parser.parse_args()

    
    image = Image.open(open(args.filename))
    # TODO: Change the image aspect ratio to compensate for funky pixel shape
    #       In the standard font, characters are roughly 7px*14px
    #ow,oh = image.size
    #image = image.resize((ow,oh/2))

    # Resize to sensible constraints.  These are finest guesswork.
    image.thumbnail((200,100), Image.ANTIALIAS)

    substitutions = build_substitutions() 

    source = image.getdata()
    width,height = image.size
    result = []
    for y in xrange(0,(height/2)*2,2):
      row = []
      for x in xrange(0,(width/2)*2,2):
        offset = (y * width) + x

        block = [source[offset],
                 source[offset+1],
                 source[offset+width],
                 source[offset+width+1]]
        row.append(best(substitutions,block)),
      result.append(row)

    output_html(result)
