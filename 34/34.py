"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

import math

nums = []
for n in range (3, 100001):
    fact_sum = 0
    for d in str(n):
        fact_sum += math.factorial(int(d))
        if fact_sum > n:
            continue
    if fact_sum == n:
        nums.append(n)

print sum(nums)
