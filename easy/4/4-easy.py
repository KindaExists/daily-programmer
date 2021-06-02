
"""
[easy] challenge #4

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
"""

# This question can be easily answered in <10 lines if done without verifications

# Not written in the question, but as an extra challenge
# I'm adding requirements for the password generator:
# - 8 or more characters (Unless specified)
# - At least number and special symbol in the password
# - At least one uppercase character and lowercase character in password

# ASCII will be used for my solution to get characters from the range 33('!') - 126('~')
# This is also kind of a brute-force solution

import random

def verify_pass(password):
    s_letter = False
    c_letter = False
    numeric = False
    special = False

    # Added to remove a few possibly problematic special characters
    exclude_str = '\\"\'<>^'

    for char in password:
        if char in exclude_str:
            continue
        elif not s_letter and char.islower():
            s_letter = True
        elif not c_letter and char.isupper():
            c_letter = True
        elif not numeric and char.isdigit():
            numeric = True
        else:
            # This works as the ascii characters in the range 33-126,
            # Excluding all alpha-numeric characters, are special characters
            special = True

    return (s_letter and c_letter and numeric and special)

if __name__ == '__main__':
    n = input('Number of Passwords: ')
    pass_len = input('Password Length: ')

    pass_list = []
    while len(pass_list) <= n:
        new_pass = ''.join([chr(random.randint(33,126)) for j in range(pass_len)])
        if verify_pass(new_pass):
            pass_list.append(new_pass)

    print(pass_list)

