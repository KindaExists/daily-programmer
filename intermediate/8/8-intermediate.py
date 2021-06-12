
"""
[intermediate] challenge #8

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/psewf/2162012_challenge_8_intermediate/
"""

# Brute-forcing 101

digits = {
    '0' : '',           '1' : 'one',
    '2' : 'two',        '3' : 'three',
    '4' : 'four',       '5' : 'five',
    '6' : 'six',        '7' : 'seven',
    '8' : 'eight',      '9' : 'nine',
}

teens_digit = {
    '0' : 'ten',        '1' : 'eleven',
    '2' : 'twelve',     '3' : 'thirteen',
    '4' : 'fourteen',   '5' : 'fifteen',
    '6' : 'sixteen',    '7' : 'seventeen',
    '8' : 'eighteen',   '9' : 'nineteen',
}

tens_digit = {
    '0' : False,        '1' : teens_digit,
    '2' : 'twenty',     '3' : 'thirty',
    '4' : 'forty',      '5' : 'fifty',
    '6' : 'sixty',      '7' : 'seventy',
    '8' : 'eighty',     '9' : 'ninety',
}

thousands_post = {
    0 : '',
    1 : '-thousand',
    2 : '-million',
    3 : '-billion',
}

def num_to_text(num):
    th_len = ((len(str(num)) - 1) // 3) + 1
    th_exp = 1000

    th_sets = [list(reversed(str((num % (th_exp**(e+1))) // (th_exp**e)))) for e in range(th_len)]

    num_builder = []

    for ind, th in enumerate(th_sets):
        th_builder = ''

        if len(th) == 1 and th[0] == '0':
            continue

        if len(th) >= 3:
            th_builder += digits[th[2]] + ' hundred'

        if len(th) >= 2:
            if th[1] != '0':
                if len(th) >= 3:
                    th_builder += ' '

                tens = tens_digit[th[1]]
                if isinstance(tens, dict):
                    th_builder += teens_digit[th[0]]
                elif isinstance(tens, str):
                    th_builder += tens
                    if th[0] != '0':
                        th_builder += '-' + digits[th[0]]

            elif len(th) >= 1 :
                th_builder += ' ' + digits[th[0]]
        elif len(th) >= 1 :
            th_builder += digits[th[0]]

        num_builder.append(th_builder + thousands_post[ind])

    return ', '.join(num_builder[::-1])

if __name__ == '__main__':
    num = int(input('Number to convert: '))
    print(num_to_text(num))

