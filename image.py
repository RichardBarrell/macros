from substitutions import build_substitutions
from PIL import Image

from math import sqrt
image = Image.open(open('/Users/alanh/Desktop/magictoad.jpg'))
# TODO: Change the image aspect ratio to compensate for funky pixel shape

# Characters are roughly 7*14
ow,oh = image.size
#image = image.resize((ow,oh/2))
image.thumbnail((200,100), Image.ANTIALIAS)
#image.show()


#import sys
#sys.exit(0)

# Fast
substitutions = build_substitutions() 

#print len(substitutions)


def best(block):
  """ Return the character best suited to represent block """
  best = None
  result = None

  for output,irc_fg,irc_bg,character in substitutions:
    error = 0
    for i in xrange(4):
      #(r1 - r2)[squared] + (g1 -g2)[squared] + (b1 - b2)[squared]
      
      #error += sum((l-r)**2 for l, r in zip(output[i], block[i]))**0.5
      
      #error += sqrt(((block[i][0] - output[i][0])**2) + ((block[i][1] - output[i][1])**2) +((block[i][2] - output[i][2])**2))
      
        
        
      for c in xrange(3):
        error += abs(block[i][c] - output[i][c])    
    if best is None or error < best:
      best = error
      result = (irc_fg,irc_bg,character)

  return result

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
    row.append(best(block)),
  result.append(row)

print result