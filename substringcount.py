'''
This is to print substring count
'''

in_string=input("Enter the main string:")
in_sub=input("Enter the substring to found the count in main string:")
sub_count=0

for i in range(0,len(in_string)):
	for j in range(i+1,len(in_string)+1):
		print(in_string[i:j])
		if in_sub==in_string[i:j]:
			sub_count+=1
print("number of instance of \"",in_sub,"\" in the \"",in_string,"\" is ",sub_count)

