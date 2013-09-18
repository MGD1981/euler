"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?"""


def get_solutions(p):
    solutions = 0
    for a in range(1, int(p/2 + 1)):
        for b in range(a, int(p/2 + 1)):
            #print "%d, %d" % (p, a + b + (a**2 + b**2)**0.5)
            if a + b + (a**2 + b**2)**0.5 == p:
                solutions += 1
    return solutions

max_perimeter = (0, 0)

for p in range(1, 1001):
    solutions = get_solutions(p)
    if solutions > max_perimeter[1]:
        max_perimeter = (p, solutions)

print max_perimeter
