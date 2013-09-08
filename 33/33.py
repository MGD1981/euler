"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""

fractions = []
for d in range(11, 100):
    for n in range(10, d):
        for char in str(n):
            if char == '0':
                continue
            if char in str(d):
                d_dig = float(str(d)[1-str(d).index(char)])
                n_dig = float(str(n)[1-str(n).index(char)])
                if d_dig == 0 or n_dig == 0:
                    continue
                if n_dig / d_dig == float(n)/float(d):
                    fractions.append((n,d))

n_prod = 1
d_prod = 1
for fraction in fractions:
    n_prod *= fraction[0]
    d_prod *= fraction[1]


print d_prod/n_prod
