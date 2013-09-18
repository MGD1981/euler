"""Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?"""


largest = 0
multiplicand = 0

while multiplicand < 10000:
    multiplicand += 1
    if multiplicand % 5 == 0:
        continue
    digits = ''
    new_length = 0
    n = 1
    while new_length < 9:
        new_product = str(multiplicand * n)
        if '0' in new_product:
            break
        new_length = len(new_product + digits)
        if new_length == len(set(new_product+digits)):
            digits += new_product
            if new_length == 9:
                largest = max(largest, int(digits))
            n += 1
        else:
            break
                 
print largest
