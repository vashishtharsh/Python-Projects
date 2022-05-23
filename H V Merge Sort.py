ev = [12,42,53,14,86,34]

def Division(ev):
    i = 0
    j = 0
    k = 0
    if len(ev) > 1:
        middle = (0 + (len(ev)//2))
        l = ev[0:middle]
        r = ev[middle:]
        Division(l)
        Division(r)

        while (i < len(l) and j < len(r)):
            if l[i] <= r[j]:
                ev[k] = l[i]
                i = i + 1
                k = k + 1
            else:
                ev[k] = r[j]
                j = j + 1
                k = k + 1
                
        while i < len(l):
               ev[k] = l[i]
               i = i + 1
               k = k + 1

        while j < len(r):
               ev[k] = r[j]
               j = j + 1
               k = k + 1

def printList(ev):
    for x in range(len(ev)):
        print(ev[x],end=" ")
    print()

# Driver Code
print("Before:",end=" ")
printList(ev)
Division(ev)
print()
print("After:",end=" ")
printList(ev)
