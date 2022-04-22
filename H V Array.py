import array as a
arr=a.array('i',[10,20,30])
l=len(arr)

for i in range(l):
    min=arr[0]
    max=arr[0]
for i in range(l):
    if arr[i]<min:
        min=arr[i]

for i in range(l):
    if arr[i]>max:
        max=arr[i]
    
print(min)
print(max)
