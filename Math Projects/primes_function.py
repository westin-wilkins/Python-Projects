
def primes(n):
    for i in range(2, n):
        if n % i == 0:
            break
        else:
            return n

N = 200

for i in range(1, N + 1):
    if (primes(i)):
        print(i, end=" ")