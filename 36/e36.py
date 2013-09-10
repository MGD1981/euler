"""The decimal number, 585 = 1001001001^2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""


def is_palindromic(n):
    nstr = str(n)
    if nstr[-1] == '0':
        return False
    for d in range(0, (len(nstr)/2)):
        if nstr[d] != nstr[-d-1]:
            return False
    return True


pals = []
for n in range(1, 1000000):
    if is_palindromic(n):
        if is_palindromic(bin(n)[2:]):
            pals.append(n)

print sum(pals)
