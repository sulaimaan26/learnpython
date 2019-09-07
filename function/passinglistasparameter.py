# count the number of odd and even from the input string
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even


lst = []
for i in range(int(input("Enter the number of numbers to count:"))):
    lst.append(int(input("Enter the number:")))
even, odd = count(lst)
print("odd : {}  and even : {}".format(even, odd))
