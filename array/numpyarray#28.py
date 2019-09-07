'''
Different ways of creating array
1. array()
2. linspace()
3. logspace()
4. arange()
5. zeros()
6. ones()

'''


from numpy import *

print("-------------------------------array()-----------------------")
#1 st way
arr=array([1,2,3,4,5])
print(arr)
print(arr.dtype)

arr=array([1,2,3,4,5.3],int)
print(arr)
print(arr.dtype)

print("-------------------------------linspace()-----------------------")
#2nd way
arr2= linspace(0,15,16)
print(arr2)
arr2= linspace(0,15) #willbe convertes 50parts by default
print(arr2)
arr2=linspace(0,15,5)
print(arr2)

print("--------------------------arange()---------------")
arr3=arange(1,15,2)
print(arr3)

print("--------------------------logspace()-----------------")
arr4=logspace(1,40,5)
print(arr4)

print("-----------zeros()---------------")
arr=zeros(5,int)
print(arr)

print("--------------------ones()-----------------")
arr=ones((3,3),int)
print(arr)