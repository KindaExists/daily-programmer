
"""
[easy] challenge #8

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/
"""

# With Extra Credit


for n in range(100, 0, -1):
    bottle = 'bottles' if n != 1 else 'bottle'
    bottle_l = 'bottles' if n-1 != 1 else 'bottle'
    print(f'{n} {bottle} of beer on the wall, {n} {bottle} of beer.', end=' ')
    print(f'Take one down and pass it around, {n-1} {bottle_l} of beer on the wall...', end=' ')

print('No more bottles of beer on the wall, no more bottles of beer.', end=' ')
print('Go to the store and buy some more, 99 bottles of beer on the wall...')