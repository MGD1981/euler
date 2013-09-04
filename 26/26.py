"""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

def unit_division(den, num=1):
    dec = []
    while den > num:
        num = num * 10
        dec.append((int(num/den),num))
        num = num - (den * dec[-1][0])
        if dec[-1] in dec [:-1]:
            return dec[dec.find(dec[-1]):-1]
        if num == 0:
            return dec 


max_length = 0
max_den = 0
for d in range(2,1001):
    dec = unit_division(d)
    print d, dec
    if len(dec) > max_length:
        max_length = len(dec)
        max_den = d
print d, max_den
