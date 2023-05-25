# n is the integer that I want to find the relatively prime numbers for
# For a number to be relatively prime to n it must have a gcd = 1. 

# Find gcd first. If gcd = 1 append to a list, else move on to the next number.

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def euler_totient(n):
    relatively_prime_numbers = []
    for i in range(1, n + 1):
        if gcd(i, n) != 1:
            pass
        else:
            relatively_prime_numbers.append(i)
    return len(relatively_prime_numbers)
        
print(euler_totient(24156))