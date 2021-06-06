
"""
[easy] challenge #5

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/
"""

# Not using the Math.PI module or PI here because it may be counted as cheating
# Also not using the Math module in general



from decimal import *

decimals = 36
q = 750

getcontext().prec = decimals

def factorial(n):
    factorial = 1
    if int(n) >= 1:
        for i in range(1, int(n)+1):
            factorial = factorial * i
    return factorial

series = []
for i in range(q):
    num = Decimal(((-1) ** i) * factorial(6 * i) * ((545140134 * i) + 13591409))
    deno = Decimal((factorial(3 * i) * (factorial(i) ** 3)) * ((-262537412640768000) ** i))
    frac = num / deno
    series.append(frac)

# num2 = 426880 * Decimal(10005 ** 1/2)
num2 = 426880 * Decimal(10005).sqrt()
largePi = (num2) / sum(series)
piStr = str(largePi)

print(largePi)

"""

enlargener = 10 ** 100
# Not sure why I'm calling this an "enlargener"
# This just allows me to use an int instead of a float and avoid floating-point imprecision

series = []
for i in range(precision):
    frac = -(((i % 2) * 2) - 1) * ((4 * enlargener) // ((((i * 2) + 3) ** 3) - ((i * 2) + 3)))
    series.append(frac)

largePi = sum(series)

piStr = f'{3}.{str(largePi)}'

print(piStr)

"""