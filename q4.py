'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
max = 0

for i in range(100, 999 + 1):
    for j in range(100, 999 + 1):
        
        prod = i*j
        prod_lst = [int(digit) for digit in str(prod)]

        stack = []

        for _ in range(0, int(len(prod_lst)/2)):
            stack.append(prod_lst.pop()) # push stuff onto the stack up to half the size of the product

        if len(prod_lst) > len(stack):
            del prod_lst[-1]

        if prod_lst == stack:
            
            if prod > max:
                max = prod

print(max)