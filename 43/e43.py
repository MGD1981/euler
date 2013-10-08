"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property."""

winners = []

def get_digits(digits=''):
    if len(digits) == 0:
        for n in range(1024, 9877, 2):
            if len(set(str(n))) != 4:
                continue
            get_digits(str(n)[0]+str(n)[1]+str(n)[2]+str(n)[3])
        print winners
        print sum(winners)
    elif len(digits) < 10:
        for d in range(0,10):
            digit = str(d)
            if digit not in digits:
                if factors_out(digits + digit):
                    get_digits(digits + digit)
    else:    
        if factors_out(digits):
            winners.append(int(''.join(digits)))

def factors_out(digit_string):
    if digit_string == None:
        return False
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    return int(digit_string[-3:]) % prime_list[len(digit_string)-4] == 0

get_digits()

