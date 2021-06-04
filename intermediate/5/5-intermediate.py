

"""
[intermediate] challenge #4

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pnhtj/2132012_challenge_5_intermediate/
"""

words = []
sorted_words = []
with open('intermediate/5/words.txt', 'r') as fp:
    words = fp.read().split()
    sorted_words = [''.join(sorted(word)) for word in words]
    fp.close()

word_dict = {}
for ind, word in enumerate(sorted_words):
    if word in word_dict:
        word_dict[word].append(words[ind])
    else:
        word_dict[word] = [words[ind]]

print('\n'.join([', '.join(word_set) for word_set in word_dict.values() if len(word_set) > 1]))
