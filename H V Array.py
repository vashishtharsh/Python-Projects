import array as a
arr=a.array('i')
n=9
for i in range (0,9):
    num=int(input())
    arr.append(num)

print(arr)

n_row=2
for i in range(0,len(arr)):
    if i%((len(arr))/n_row)==0:
        print()
        print(arr[i],end="")
