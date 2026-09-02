#main program
import item

print("Hello User")

def buyingItem(product):
    product.sold(1)

I1 = item.item("soda", 3.44, 4)
print(I1.show())
I1.sold()
print(I1.show())