#Main Program
from item import item
from Stack import Stack

print("Hello User")

historyStack = Stack()


def displayOptions():
    pass

def buyingItem(product):
    product.sold(1)
    historyStack.push(f'{product.getName()} was sold for {product.getPrice()}')

def buyStock(product, n):
    pass

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