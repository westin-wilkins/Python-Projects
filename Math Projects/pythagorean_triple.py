for x in range(3, 101):
    for y in range(3, 101):
        for z in range(3,101):
            if x**2 + y**2 == z**2:
                print(x,y,z)