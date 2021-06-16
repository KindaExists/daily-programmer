
"""
[easy] challenge #11

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/
"""

from datetime import datetime

if __name__ == '__main__':
    days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

    date = [int(input()) for i in range(3)][::-1]
    print(days[datetime(*date).weekday()])