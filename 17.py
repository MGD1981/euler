#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

letters = 0
for n in range(1, 1001):
    n = str(n)
    for i in range(1, len(n)+1):
        x = n[-i]

        if i in [1,3,4]: # 1's, 100's, 1000's place
            if x in ['1','2','6']:
                letters += 3
            if x in ['4','5','9']:
                letters += 4
            if x in ['3','7','8']:
                letters += 5

        if i == 2: # 10's place
            if x == '1': # teens
                if n[-1] in ['4','6','7','9']:
                    letters += 4
                else:
                    letters += 3
            if x in ['4','5','6']:
                letters += 5
            if x in ['2','3','8','9']:
                letters += 6
            if x == '7':
                letters += 7

        if i == 3 and x != '0': # 'hundred (and)'
            if n[-2] == '0' and n[-1] == '0':
                letters += 7
            else:
                letters += 10

        if i == 4: # 'thousand'
            letters += 8

print letters
