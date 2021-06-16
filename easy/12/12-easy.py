
"""
[easy] challenge #12

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pxs2x/2202012_challenge_12_easy/
"""

# I mean I'm pretty sure this is about what was expected
# Admittedly my solution is very similar to what some others did
# However my solution prints them in different lines
# (I believe its much more in-line with the specs of the challenge)

# In any case also check out the solutions of "u/JerMenKoO" and "u/SleepyTurtle" as well

from itertools import permutations
[print(''.join(p)) for p in permutations(input('Text to permutate: '))]