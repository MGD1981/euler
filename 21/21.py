"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

def d(n):
    assert type(n) == int and n > 0
    divisors = []
    for x in range(1, (n/2)+1):
        if n % x == 0:
            divisors.append(x)
    return sum(divisors)

d_hash = {}
for n in range(1, 10000):
    d_hash[n] = d(n)

amicables = []
for key in d_hash:
    val = d_hash[key]
    if val not in d_hash or key == val:
        continue
    elif key == d_hash[val]:
        print "Pair: %d | %d" % (key, val)
        amicables.append(val)

print sum(amicables)
