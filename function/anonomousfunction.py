from functools import *
# sum=lambda a,b:a+b

# print(sum(5,4))

##using lamba in other function map() reduce() filter()

# using filter
lst = [1, 2, 3, 4, 5, 6, 78, 99]

evennumber = list(filter(lambda n: n % 2 == 0, lst))
print("Even number is ", evennumber)

addplustwo=list(map(lambda add: add+2, lst))
print("Sum of number is",addplustwo)

addtwonumer=reduce(lambda a,b: a+b, lst)
print("sum of numbers in list",addtwonumer)
