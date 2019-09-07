def getfib(n):
    stay = []
    if (n > 0):

        a = 0
        b = 1
        c = 0
        stay.append(str(a))
        stay.append(str(b))
        for _ in range(n):
            stay.append(',')
            c = a + b
            a, b = b, c
            stay.append(str(c))
    else:
        stay.append("Please enter the valid number")
    return stay


n = int(input("Enter the number of fibonacci series to be generated:"))
print("Generated Fibonacci series is ", end="")
for i in range(len(getfib(n))):
    print(getfib(n)[i], end="")
