a = 10
b=5

def samplefunction():
    a = 5
    print("From function", a)
    print(globals())
    globals()['a'] = 12


samplefunction()
print("outside the function", a)
