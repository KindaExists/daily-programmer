
myStr = '3.141592653589741586517727315459'
comparisonStr = '3.1415926535897932384626433'

correct = ''
for ind, char in enumerate(myStr):
    if char == comparisonStr[ind]:
        correct += char
    else:
        print('wrong')
        break

print(correct)