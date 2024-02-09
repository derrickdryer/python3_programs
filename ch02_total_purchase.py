item1 = float(input("Enter price for item 1: "))
item2 = float(input("Enter price for item 2: "))
item3 = float(input("Enter price for item 3: "))
item4 = float(input("Enter price for item 4: "))
item5 = float(input("Enter price for item 5: "))

subTotal = item1 + item2 + item3 + item4 + item5

salesTax = subTotal * 0.07

total = subTotal + salesTax

print("Subtotal: $", format(subTotal, '.2f'))
print("Sales Tax: $", format(salesTax, '.2f'))
print("Total: $", format(total, '.2f'))
