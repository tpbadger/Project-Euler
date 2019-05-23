'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

def isPrime(n):
    '''
    Check if n is prime
    '''

    if n == 1 or n == 2:
       
        return True 
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

def nextPrime(n):
    '''
    Return the next prime number after n
    '''

    n += 1 # add one so doesnt just return n if it is prime

    while not isPrime(n):
        n += 1

    return n

def sumPrime(n):
    '''
    Find the sum of all primes less than n
    '''

    curr_prime = 1
    total = 0

    while curr_prime < n:
        curr_prime = nextPrime(curr_prime)
        if curr_prime > n:
            break
        total += curr_prime

    return total

print(sumPrime(2000000))


