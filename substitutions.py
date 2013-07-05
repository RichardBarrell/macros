# -*- coding: utf-8 -*-

# # Build a list of substitutions

# IRC colour to colour (mIRC colours)
COLOURS = {0:(255,255,255),
           1:(0,0,0),
           2:(0,0,255),
           3:(0,128,0),
           4:(255,0,0),
           5:(128,64,64),
           6:(128,0,255),
           7:(128,128,0),
           8:(255,255,79),
           9:(0,255,0),
           10:(0,128,128),
           11:(0,255,255),
           12:(0,0,255),
           13:(255,0,255),
           14:(128,128,128),
           15:(192,192,192),}

# Colloquy colours
XCOLOURS = {0:(255,255,255),
          1:(0,0,0),
          2:(0,0,123),
          3:(0,147,0),
          4:(255,0,0),
          5:(123,0,0),
          6:(156,0,156),
          7:(255,123,0),
          8:(255,255,0),
          9:(0,255,0),
          10:(0,147,147),
          11:(0,255,255),
          12:(0,0,255),
          13:(255,0,255),
          14:(123,123,123),
          15:(214,214,214),}


# Character to coverage
MASKS = {'▖':(0,0,1,0),
         '▗':(0,0,0,1),
         '▘':(1,0,0,0),
         '▝':(0,1,0,0),
         '▙':(1,0,1,1),
         '▚':(1,0,0,1),
         '▛':(1,1,1,0),
         '▜':(1,1,0,1),
         '▞':(0,1,1,0),
         '▟':(0,1,1,1),}

MASKS = {'\xe2\x96\x97': (0, 0, 0, 1),
         '\xe2\x96\x96': (0, 0, 1, 0),
         '\xe2\x96\x9b': (1, 1, 1, 0),
         '\xe2\x96\x9a': (1, 0, 0, 1),
         '\xe2\x96\x99': (1, 0, 1, 1),
         '\xe2\x96\x98': (1, 0, 0, 0),
         '\xe2\x96\x9f': (0, 1, 1, 1),
         '\xe2\x96\x9e': (0, 1, 1, 0),
         '\xe2\x96\x9d': (0, 1, 0, 0),
         '\xe2\x96\x9c': (1, 1, 0, 1)}

def build_substitutions():
    result = []
    for character,mask in MASKS.items():
        for irc_foreground,foreground in COLOURS.items():
            for irc_background,background in COLOURS.items():
                # We'll do the block colour for each colour separately
                if irc_foreground == irc_background:
                    continue
                
                block = []
                for bit in mask:
                    if bit:
                        block.append(foreground)
                    else:
                        block.append(background)
                
                result.append((block,irc_foreground,irc_background,character))
    
    # Do block colour (bg = fg)
    for irc_colour,colour in COLOURS.items():
        result.append(((colour,colour,colour,colour),irc_colour,irc_colour,'▟'))
    
    return result
                    



