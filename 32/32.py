"""is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum."""

used = []
products = []
for a in range(1, 10000):
    used.append(a)
    if '0' in str(a):
        continue
    for b in range(1, 10000):
        if '0' in str(b):
            continue
        p = a*b
        if '0' in str(p):
            continue
        digs_used = len(set(str(a)+str(b)+str(p))) 
        if digs_used != 9 or digs_used < len(str(a)+str(b)+str(p)):
            continue
        if b in used:
            break
        if p not in products:
            products.append(p)


print sum(products)
