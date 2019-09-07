# Keyword variable length arguments
def person(name, **otherdetail):
    print(name)
    print(otherdetail)


person('sulaimaan', age=4, number=7299508683, city='chennai')
