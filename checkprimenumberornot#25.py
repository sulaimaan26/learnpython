x=int(input("Enter the number to check prime number or not:"));

for i in range(2,x):
	#print(i)
	if(x%i)==0:
		print(x,"is not a prime number")
		print(i)
		break
else:
	print(x,"is a prime number")