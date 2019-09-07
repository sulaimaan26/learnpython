from array import *
x=int(input("Enter the length of the array"))

v=array('i',[])
for i in range(x):
	values=int(input("Enter the values for the array"))
	v.append(values)

print(v)

valuessearch=int(input("Enter the values to be get index from the array "))

k=0
for e in v:
	if e==valuessearch:
		print("Index of given number in array is ",k)
		break

	k+=1


print(v.index(valuessearch))