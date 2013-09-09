"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

def is_prime(n):
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


circular_primes = [2]
for num in range(3, 1000000):
    if '0' in str(num):
        continue
    add = True
    n = num 
    for _ in range(0, len(str(num))):
        if is_prime(n):
            n = int(str(n)[1:]+str(n)[0])
        else:
            add = False
            break
    if add == True:
        circular_primes.append(num)

print len(circular_primes)
