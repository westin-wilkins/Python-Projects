def gcf(num1, num2):
    factorList1 = []
    factorList2 = []
    
        # Finds the factors of num1
    for i in range(1, num1 + 1): 
        if num1 % i == 0:
            factorList1.append(i)
        # Finds the factors of num2    
    for i in range(1, num2 + 1):  
        if num2 % i == 0:
            factorList2.append(i)
        # Prints the intersection of num1 and num2 
    intersection = set(factorList1).intersection(factorList2)
    return (max(intersection))

print(gcf(30, 50))