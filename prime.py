num=int (input("Enter the prime number:"))
k=0
if num==0 or num==1:
   k=1
else:
    i=2
    while (i<num):
        if num%i==0:
           k=k+1
        i=i+1
if k==0:
    print ("prime number")
else:
    print ("not a prime number")
