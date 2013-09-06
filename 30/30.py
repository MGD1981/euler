"""Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

fifth_power_nums = []

for n in range(2, 9**5 + 9**5 + 9**5 + 9**5 + 9**5):
    nsum = 0
    for d in str(n):
        nsum += int(d)**5
    if nsum == n:
        fifth_power_nums.append(n)

print fifth_power_nums
print sum(fifth_power_nums)
