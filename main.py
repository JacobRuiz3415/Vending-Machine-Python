#Main Program
from item import item
from Stack import Stack

print("Hello User")

historyStack = Stack()
itemList = []

def selectItem():
    pass

def displayOptions():
    pass

def buyingItem(product):
    product.sold(1)
    historyStack.push(f'{product.getName()} was sold for {product.getPrice()}')

def buyStock(product, n):
    product.restock(n)
    historyStack.push(f'{product.getName()} was restock by {n}')

def readItemListFile():
    f = open("itemList", "r")
    lines = f.readlines()

    print(lines)


I1 = item("soda", 3.44, 4)
print(I1.show())
# I1.sold()
buyingItem(I1)
print(I1.show())
print(historyStack.pop())
#testing output to a file
f = open("history", "w")
f.write(I1.show())

#read the file
f = open("history")
print(f.read())