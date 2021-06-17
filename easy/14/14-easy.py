
"""
[easy] challenge #14

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/q2v2k/2232012_challenge_14_easy/
"""

a = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2
print([x for i in range(0, len(a), k) for x in a[i:i+k][::-1]])
