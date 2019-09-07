'''
using for else loop to find number divisible by 5if not should print "not found" one time
'''

x=[1,2,3,4,1]

for i in x:
	
	if i%5 == 0:
		print(i)
		break
else:
	print("not found")