a=int(input("Enter the starting point: "))
b=int(input("Enter the ending point: "))
for i in range(a, b):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)