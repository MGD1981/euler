# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

exponent = 1000
num_a = [2]
carry = False

for _ in range(1, exponent):
    new_num = []
    num_a.reverse()
    for digit in num_a:
        product = 2 * digit
        if carry == True:
            product += 1
        carry = False
        if product >= 10:
            carry = True
            product -= 10
        new_num.append(product)
    if carry == True:
        new_num.append(1)
        carry = False
    new_num.reverse()
    num_a = new_num    

print sum(num_a)
