'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def primeFactors(n):

    factors = []

    while n % 2 == 0:
        n/=2
        factors.append(2)
    
    for divisor in range(3, int(math.sqrt(n)) + 1, 2):
        while n % divisor == 0:
            n /= divisor
            factors.append(divisor)

    if n > 2:
        factors.append(n)

    return max(factors)


print(primeFactors(600851475143))