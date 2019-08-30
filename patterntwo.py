x = 5
print(range(x))
for i in range(x, 0, -1):
    # print(i)
    for j in range(i):
        print(i, end="")
    print("")
