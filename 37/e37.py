"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

def is_prime(n): 
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for factor in range(3, int(n**0.5 + 1), 2):
        if n % factor == 0:
            return False
    return True

def is_left_truncatable(n):
    while is_prime(n):
        if n >= 10:
            n = int(str(n)[1:])
        else:
            return True
    return False

def is_right_truncatable(n):
    while is_prime(n):
        if n >= 10:
            n = int(str(n)[:-1])
        else:
            return True
    return False

trunc_primes = []

n = 11
done = False
while done == False:
    if is_left_truncatable(n) and is_right_truncatable(n):
        print n
        trunc_primes.append(n)
        if len(trunc_primes) == 11:
            done = True
    n += 2

print sum(trunc_primes)
