
"""
[easy] challenge #3

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
"""

# This can most likely be done in less than 2 lines
# However still haven't figured a way to stop asking  "shift" input

def encrypt(string, shift):
    return ''.join([chr((((ord(char) - 97) + shift) % 26) + 97) if char.isalpha() else char for char in string])


# Actually only the encrypt function is technically needed, as it can both do encrypt(+shift) and decrypt(-shift)
# However for the sake of simplicity and formality I just seperated the functionalities
def decrypt(string, unshift):
    return ''.join([chr((((ord(char) - 97) - unshift) % 26) + 97) if char.isalpha() else char for char in string])

if __name__ == '__main__':
    method = input('(e)ncrypt / (d)ecrypt?: ')
    text_in = input('String to encrypt: ')
    shift = int(input('Shift by: '))

    if method == 'e':
        print(f'> output: {encrypt(text_in, shift)}')
    elif method == 'd':
        print(f'> output: {decrypt(text_in, shift)}')
