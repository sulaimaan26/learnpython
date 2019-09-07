import sys
sys.setrecursionlimit(20000)
print(sys.getrecursionlimit())
def greet(n):
    n += 1
    print("Happy Weekend", n)
    greet(n)


greet(1)
