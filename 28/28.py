"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

*21* 22  23 24 *25*
20  *7*  8  *9* 10
19   6  *1*  2  11
18  *5*  4  *3* 12
*17* 16  15 14 *13*

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""

dist = 2
times = 0
tick = 0
nums_counted = [1]

for n in range (2, (1001*1001+1)):
    tick += 1
    if tick == dist:
        nums_counted.append(n)
        tick = 0
        times += 1
        if times == 4:
            dist += 2
            times = 0
            
print sum(nums_counted)
