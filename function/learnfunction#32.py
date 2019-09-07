def greet():
	print("Hello")

def add(x,y):
	return(x+y)

def add_sub(x,y):
	return (x+y),(x-y)


greet()
result=add(4,5)
print(result)

r1,r2=add_sub(3,2)

print(r1,r2)