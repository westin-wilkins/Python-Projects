def fibonacci(n):
    if n <= 0:
        print("Invalid number.")
    elif n == 1:
        print(f"Fibonacci sequence up to {n}:")
        print(0)
    else:
        print(f"Fibonacci sequence up to {n}:")
        fib = [0, 1]
        for i in range(2, n):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib

print(fibonacci(20))