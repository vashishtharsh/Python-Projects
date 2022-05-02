print("Without Slicing")
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s= "Harsh"
print (reverse(s))

print("*****************")

print(">>>>>With Slicing<<<<<")
def reverse1(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:]) + s[0]
print (reverse1(s))

print("******************")
print(">>>>>With Slicing<<<<<")

a=len(s)
b=s[a::-1]
print (b)
