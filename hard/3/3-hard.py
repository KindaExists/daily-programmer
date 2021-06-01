
"""
[hard] challenge #3

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pkwgf/2112012_challenge_3_difficult/
"""

#! Note: I have no experience with cyphers, as such my solution here may be wrong
# However, from what I understand the given are just scrambled versions of words present in the "wordlist.txt" file
# And the program has to find the matching words


# The solution I wrote down here uses a sorting method to match letters from scrambled list -> unscrambled list
# Although the issue with this solution is if there are multiple sets of words that have a simillar set of letters
# ex. Wrong <-> Grown
# This means using "list.index()" may not be a good idea, and a different method should be used in future revisions


# Pre-processing
word_list = []
sorted_list = []
with open('hard/3/wordlist.txt', 'r') as f:
    word_list = f.read().split()
    sorted_list = [''.join(sorted(word)) for word in word_list]
    f.close()

if __name__ == '__main__':
    scrambled = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle', 'nalraoci', 'nsdeuto', 'amrhat', 'inknsy', 'iferkna']
    out_list = []

    for word in [''.join(sorted(word)) for word in scrambled]:
        out_list.append(word_list[sorted_list.index(word)])

    out_list = sorted(out_list, key=lambda x:len(x))

    for word in out_list:
        print(word)
