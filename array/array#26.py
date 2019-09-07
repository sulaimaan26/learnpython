from array import *

x=array("i",[1,2,3,4])

copy_x=array(x.typecode,(a*a for a in x))
for i in copy_x:
	print(i)