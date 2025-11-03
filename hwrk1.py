import random

rice_price = 45.0
sugar_price = 40.0
oil_price = 130.0

rice_qty = 3.0
sugar_qty = 2.5
oil_qty = 1.8

rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty
total_bill = rice_total + sugar_total + oil_total

print("Rice Total: ₹", rice_total)
print("Sugar Total: ₹", sugar_total)
print("Oil Total: ₹", oil_total)

print("\nTotal Bill (float): ₹", total_bill)

total_bill_int = int(total_bill)
print("Total Bill (integer): ₹", total_bill_int)

total_bill_str = str(total_bill)
print("Total Bill as string: ₹" + total_bill_str)

delivery_charge = random.randint(5, 10)
final_bill = total_bill + delivery_charge
print("\nDelivery Charge: ₹", delivery_charge)
print("Final Bill (including delivery): ₹", final_bill)
