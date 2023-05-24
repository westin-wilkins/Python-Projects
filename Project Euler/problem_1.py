# Find the sum of all the multiples of 3 and 5 below 1000.

multiples = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples += i
print(multiples)