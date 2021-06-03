
"""
[easy] challenge #5

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/
"""

# Can't do extra extra credit, cause I have no clue how to do that yet


import getpass

user = input('Username: ')
pwd = getpass.getpass('Password: ')

with open('easy/5/passwd.txt', 'r') as fp:
    p = fp.read().split(' ')
    if user == p[0] and pwd == p[1]:
        print('User Verified')
    else:
        print('User Invalid')

