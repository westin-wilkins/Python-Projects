# The Collatz Conjecture states that any integer n will eventually reduce to 1 after a number of operations.
# The program continously divides n by 2 if even and multiply by 3 plus 1 if odd.
# The program stops once n = 1 and prints out the series.

def collatz_conjecture(n):
    values = [n]
    while n != 1:
        if n % 2 == 0: # Case when n is even
            n = n // 2
        else:
            n = 3 * n + 1 # Case when n is odd
        values.append(n) 
    return values

print(collatz_conjecture(25))
