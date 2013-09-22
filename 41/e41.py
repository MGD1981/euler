"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""


def is_pandigital(n):
    digits = []
    n_str = str(n)
    n_len = len(n_str)
    for d in n_str:
        if d == '0' or int(d) > n_len or d in digits:
            return False
        digits.append(d)
    return True

def is_prime(n):
    if n == 2 or n == 1:
        return True
    divisor = 3
    max_divisor = int(n*0.5) + 1
    while divisor < max_divisor:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

n = 7654321
while n > 0:
    if is_pandigital(n):
        if is_prime(n):
            print n
            break
    n -= 2

