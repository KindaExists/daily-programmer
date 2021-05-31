
"""
[easy] challenge #1

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
"""

#! Assuming users input correct values 
name = input('What is your name?: ')
age = input('What is your age?: ')
user = input('What is your username?: ')

# For Simple Solution
# print(f'your name is {name}, you are {age} years old, and your username is {user}')

# For Advanced Solution

with open('easy/1/log.txt', 'a') as f:
    f.write(f'{name}, {age}, {user}\n')
    f.close()