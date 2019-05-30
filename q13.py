'''
The following iterative sequence is defined for the set of positive integers:

n n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:


It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def is_even(n):
    return int(n/2)


def is_odd(n):
    return int(3*n + 1)


seen = {}

start_num = 13
chain_length = 1 # always end in 1

n = start_num



if start_num not in seen.values():
    while n != 1:
        if n % 2 == 0:
            n = is_even(n)
        else:
            n = is_odd(n)
        chain_length += 1
    seen[str(start_num)] = chain_length
else:
    chain_length += seen.find(str(n))

print(seen)






