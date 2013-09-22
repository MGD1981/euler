"""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000"""


def nth_digit(n):
    num_str = '0.'
    ordinal = 1
    dec_length = 0

    while dec_length < n:
        ordinal_str = str(ordinal)
        num_str += ordinal_str
        dec_length += len(ordinal_str)
        ordinal += 1

    return int(num_str[-1 - (dec_length - n)])


print (nth_digit(1) * nth_digit(10) * nth_digit(100) * nth_digit(1000) * 
       nth_digit(10000) * nth_digit(100000) * nth_digit(1000000))
