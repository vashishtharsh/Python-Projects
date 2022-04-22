def linear(a, target):
    for i in range(0,len(a)):
      if target == a[i]:
        print(i)
        return
    print(-1);
a=[4,0,6,3,4]
linear(a,7)
