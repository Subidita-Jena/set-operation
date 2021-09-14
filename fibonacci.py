n = int (input("enter how many numbers you want in this series:"))
a = 0
b = 1
for i in range(n):
    print(a)
    temp = a
    a = b
    b = temp + b