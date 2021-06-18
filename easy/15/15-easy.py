
"""
[easy] challenge #15

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/q4c34/2242012_challenge_15_easy/
"""

with open('easy/15/text.txt', 'r+') as fp:
    x = input('(L)eft/(R)ight-justified: ').lower()
    text_char_len = int(input('Total character length: '))
    lines = [getattr(line.strip(), f'{x}just')(text_char_len) + '\n' for line in fp.readlines()]
    fp.seek(0)
    fp.writelines(lines)
    fp.close()