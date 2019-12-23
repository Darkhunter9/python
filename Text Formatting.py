from math import ceil, floor
import re

def text_formatting(text: str, width: int, style: str) -> str:
    words = text.split(' ')
    lines = []
    line = ''

    while words:
        while words and (len(line) <= width - len(words[0]) - 1 or not line):
            if not line:
                line += words.pop(0)
            else:
                line += ' '+words.pop(0)
        lines.append(line)
        line = ''

    for i in range(len(lines)):
        # if style == 'l' and i != len(lines)-1:
        #     lines[i] = lines[i] + ' '*(width-len(lines[i]))
        if style == 'r':
            lines[i] = ' '*(width-len(lines[i])) + lines[i]
        elif style == 'c':
            lines[i] = ' '*floor((width-len(lines[i]))/2) + lines[i]
        elif style == 'j' and i != len(lines)-1:
            space = width-len(lines[i])
            a = space//lines[i].count(' ')
            b = space%lines[i].count(' ')
            lines[i] = lines[i].replace(' ', ' '*(a+1))
            lines[i] = lines[i].replace(' '*(a+1), ' '*(a+2), b)
            
    # print ('\n'.join(lines))
    return '\n'.join(lines)

if __name__ == '__main__':
    text_formatting("Oh, my sweet summer child, what do you know of fear? Fear is for the winter, my little lord, when the snows fall a hundred feet deep and the ice wind comes howling out of the north. Fear is for the long night, when the sun hides its face for years at a time, and little children are born and live and die all in darkness while the direwolves grow gaunt and hungry, and the white walkers move through the woods.",10,"c")
    LINE = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure '
            'harum suscipit aperiam aliquam ad, perferendis ex molestias '
            'reiciendis accusantium quos, tempore sunt quod veniam, eveniet '
            'et necessitatibus mollitia. Quasi, culpa.')

    print('Example:')
    print(text_formatting(LINE, 38, 'l'))

    assert text_formatting(LINE, 38, 'l') == \
        '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit. Iure
harum suscipit aperiam aliquam ad,
perferendis ex molestias reiciendis
accusantium quos, tempore sunt quod
veniam, eveniet et necessitatibus
mollitia. Quasi, culpa.''', 'Left 38'

    assert text_formatting(LINE, 30, 'c') == \
        ''' Lorem ipsum dolor sit amet,
consectetur adipisicing elit.
 Iure harum suscipit aperiam
  aliquam ad, perferendis ex
     molestias reiciendis
accusantium quos, tempore sunt
   quod veniam, eveniet et
   necessitatibus mollitia.
        Quasi, culpa.''', 'Center 30'

    assert text_formatting(LINE, 50, 'r') == \
        '''           Lorem ipsum dolor sit amet, consectetur
     adipisicing elit. Iure harum suscipit aperiam
   aliquam ad, perferendis ex molestias reiciendis
       accusantium quos, tempore sunt quod veniam,
 eveniet et necessitatibus mollitia. Quasi, culpa.''', 'Right 50'

    assert text_formatting(LINE, 45, 'j') == \
        '''Lorem   ipsum  dolor  sit  amet,  consectetur
adipisicing elit. Iure harum suscipit aperiam
aliquam    ad,   perferendis   ex   molestias
reiciendis  accusantium  quos,  tempore  sunt
quod   veniam,   eveniet   et  necessitatibus
mollitia. Quasi, culpa.''', 'Justify 45'