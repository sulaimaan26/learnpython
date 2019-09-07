#postion
def update(a,b):
	print(a+1)
	print(b)


update(2,'string')
#update('string',2) shows error this is works on position


#keyword
def enter(name,age):
	print(name)
	print(age+5)

enter(age=25,name='sulaimaan')


#default
def enter(name,age=2):
	print(name)
	print(age+5)

enter('karthi')

#length
def sum(a,*b):
	print(a)
	print(b)
	#print(a+b)

sum(1,2,3,4)



