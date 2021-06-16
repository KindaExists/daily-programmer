
"""
[intermediate] challenge #9

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pu1y6/2172012_challenge_9_intermediate/
"""


# Not going to lie, this is a cheap method but it works

if __name__ == '__main__':
    text = ''

    find_content = input()
    with open('intermediate/9/words.txt', 'r') as fp:
        text = fp.read()
        fp.close()


    # Actually it would be better if this was done in one go
    # However the phrasing of this challenge most likely entails(means) this shouldn't be done

    replace_content = input()
    with open('intermediate/9/words.txt', 'w') as fp:
        text = text.replace(find_content, replace_content)
        fp.write(text)
        fp.close()
