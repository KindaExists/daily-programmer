

"""
[easy] challenge #10

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
"""

import re

if __name__ == '__main__':
    phone = input()


    if re.match(r'(?:[(]\d{3}[)]( ?)\d{3}-\d{4})|(?:\d{3}-\d{3}-\d{4})|(?:\d{3}\.\d{3}\.\d{4})|(?:\d{10})|(?:\d{3}-\d{4}\Z)',
        phone):
        print('Number Valid')
    else:
        print('Number Invalid')