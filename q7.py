'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

def getPrime(n):
    '''
    Return the nth prime number
    '''

    curr_prime = 1
    curr_n = 0

    while curr_n < n:
        curr_prime = nextPrime(curr_prime)
        curr_n += 1
    
    return curr_prime

print(getPrime(10001))


