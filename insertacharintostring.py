actual_string = input("Enter the string for operation:")
insert_char = input("Enter the character to be insert:")
change_char = input("Enter the character to be changed:")
l = list(actual_string)
# print(l)
# print(l.index("u"))
#print(l.count(change_char))
if l.count(change_char) > 1:
    print("There is more number of character specified")
else:
    l[l.index(change_char)] = insert_char
    actual_string = "".join(l)
    print(actual_string)
