n = int(input("Enter the number"))

if n < 0:
    print(0)
elif n == 0 or n == 1:
    print(1)
else:
    fact = 1
    while(n > 1):
        fact *= n
        n -= 1
    print(fact)