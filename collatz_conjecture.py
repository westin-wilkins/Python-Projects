def collatz_conjecture(n):
    values = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        values.append(n)
    return values

print(collatz_conjecture(25))