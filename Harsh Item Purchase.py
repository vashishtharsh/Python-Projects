user= int (input("Enter the number of item you purchased"))
item1= int(input("Enter the cost of the item 1"))
item2= int(input("Enter the cost of the item 2"))
item3= int(input("Enter the cost of the item 3"))
add= item1+item2+item3
if (add>8000):
    discount = add*30/100
    print ("Your total is :" ,add-discount)
else:
    print ("Your total is: " , add)
