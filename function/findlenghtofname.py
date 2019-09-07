def findlongstring(lst):
    temp = []
    for i in range(len(lst)):
        temp.append(len(lst[i]))

    return lst[temp.index(max(temp))]


list = []
for i in range(int(input("Enter the number of students:"))):
    list.append(input("Enter the student name {}:".format(i+1)))

print("Student with largest name is {}".format(findlongstring(list)))
