#Main Program
from item import item

print("Hello User")

def buyingItem(product):
    product.sold(1)

I1 = item.item("soda", 3.44, 4)
print(I1.show())
I1.sold()
print(I1.show())

#testing output to a file
f = open("history", "w")
f.write(I1.show())

#read the file
f = open("history")
print(f.read())