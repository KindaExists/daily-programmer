
"""
[easy] challenge #9

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/
"""

nums = input('Input words/numbers (Not both) to arrange (seperated by a " "): ')
print(', '.join(sorted(nums.split(' '), key=int if nums[0].isdigit() else str)))