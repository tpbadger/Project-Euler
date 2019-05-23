'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# quick maths....

# a = 1000 - b - c
# a < b < c

# 1000 - b - c < b
# 1000 - c < 2b


# c > 1000 - 2b

# c > b 

# 1000 - 2b > b

# b < 1000/3

# c > 1000 - 2000/3

# a = 1000 - b - c

break_loop = False

for c in range(int(1000/3) + 1, 10000000):
    for b in range(2, int(1000/3) + 1):
        a = 1000 - b - c
        if (a**2 + b**2 == c**2):
            print(a * b * c)
            break_loop = True
            break
    
    if break_loop:
        break




