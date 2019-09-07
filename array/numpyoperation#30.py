from numpy import * 
#vectorized operation
arr=array([1,2,3,5,4])
print(arr)

arr2=arr.view()#shallow copy
arr[1]=9
print(arr2)
arr2=arr.copy()# Deep copy

print(arr2)
print(arr+5)

arr2=arr+5

print(arr+arr2)

print(sort(arr))

#print(concatenate(arr,arr2))