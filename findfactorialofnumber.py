def getfactorial(input):
    a = 1
    for i in range(1, input + 1):
        a *= i
    return a


n = int(input("Enter the number"))
print("Factorial of number {} is {}".format(n, getfactorial(n)))
