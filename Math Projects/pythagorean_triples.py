
def pythagorean_triples(n):
    for z in range(3, n+1):
        for y in range(3, z):
            for x in range(3, y):
                if x**2 + y**2 == z**2:
                    print(x, y, z)

pythagorean_triples(200)
