"""
Pattern print
    APQR
    ABQR
    ABCR
    ABCC

"""

x = 5
for i in range(1, x):
    for j in range(1, x):
        if j == 1:
            print("A", end="")
        # print(i, end="")
        elif j == 2 and i == 1:
            print("P", end="")
        elif j == 2:
            print("B", end="")
        elif j == 3 and i <= 2:
            print("Q", end="")
        elif j == 4 and i <= 3:
            print("R", end="")
        else:
            print("C", end="")

    print("")
