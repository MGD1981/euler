"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""


def get_factors(num):
    factors = [1]
    for n in range (2, int(num**0.5)+1):
        if num % n == 0:
            factors.append(n)
            if num/n != n:
                factors.append(num/n)
    return factors

abundants = []
for n in range(1, 28124):
    if sum(get_factors(n)) > n:
        abundants.append(n)

answer_list = []

abundants.sort()
abundant_sums = []
i =-1
for a in abundants:
    i += 1
    for b in abundants[i:]:
        abundant_sums.append(a + b)

abundant_sums_set = set(abundant_sums)
abundant_sums_list = list(abundant_sums_set)
abundant_sums_list.sort()
z = len(abundant_sums_list)
i = 0
for n in range(1, 28125):
    if n == abundant_sums_list[i]:
        i += 1
        if n == abundant_sums_list[-1]:
            break
    else:
        answer_list.append(n)

print sum(answer_list)
        
