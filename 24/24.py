"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

digs = [0,1,2,3,4,5,6,7,8,9]
place_counts = []
sum = 0

while sum < 1000000:
    n = 1
    for i in range(1, len(digs) + 1):
        if n * i >= (1000000 - sum):
            place_counts.append(i)
            break
        n = n * i

    sum += n

place_counts.pop()
ticks = []
for i in range(0, len(digs)):
    ticks.append(0)

for d in place_counts:
    ticks[len(digs)-d] += 1


perm = []
for i in range(0, len(ticks)):
    for d in range(0, 10):
        if d in perm[:i]:
            continue
        else:
            if ticks[i] == 0:
                perm.append(d)
                break
            else:
                ticks[i] -= 1

print perm
