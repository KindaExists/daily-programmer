
"""
[easy] challenge #7

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/
"""

morse_to_char = {
    '.-' : 'A',     '-...' : 'B',
    '-.-.' : 'C',   '-..' : 'D',
    '.' : 'E',      '..-.' : 'F',
    '--.' : 'G',    '....' : 'H',
    '..' : 'I',     '.---' : 'J',
    '-.-' : 'K',    '.-..' : 'L',
    '--' : 'M',     '-.' : 'N',
    '---' : 'O',    '.--.' : 'P',
    '--.-' : 'Q',   '.-.' : 'R',
    '...' : 'S',    '-' : 'T',
    '..-' : 'U',    '...-' : 'V',
    '.--' : 'W',    '-..-' : 'X',
    '-.--' : 'Y',   '--..' : 'Z',
    '/' : ' '
}

char_to_morse = {
    'A' : '.-',     'B' : '-...',
    'C' : '-.-.',   'D' : '-..',
    'E' : '.',      'F' : '..-.',
    'G' : '--.',    'H' : '....',
    'I' : '..',     'J' : '.---',
    'K' : '-.-',    'L' : '.-..',
    'M' : '--',     'N' : '-.',
    'O' : '---',    'P' : '.--.',
    'Q' : '--.-',   'R' : '.-.',
    'S' : '...',    'T' : '-',
    'U' : '..-',    'V' : '...-',
    'W' : '.--',    'X' : '-..-',
    'Y' : '-.--',   'Z' : '--..',
    ' ' : '/'
}


def decode(morse_str):
    str_builder = ''
    for code in morse_str:
        str_builder += morse_to_char[code]

    return str_builder

def encode(char_str):
    str_builder = []
    for char in char_str:
        str_builder.append(char_to_morse[char])

    return ' '.join(str_builder)

if __name__ == '__main__':
    morse = input('Morse Text: ').split(' ')
    print(decode(morse))

    string = input('Text to encode into Morse: ').upper()
    print(encode(string))


























