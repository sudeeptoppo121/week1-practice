name = input("Enter Customer Name: ")
units = int(input("Enter Number of Units Consumed: "))
if units <= 100:
    charge = units * 2
elif units <= 200:
    charge = (100 * 2) + ((units - 100) * 3)
else:
    charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

if charge > 1000:
    surcharge = charge * 0.05
else:
    surcharge = 0

final_bill = charge + surcharge
print(f"Customer Name: {name}")
print(f"Units Consumed: {units}")
print(f"Total Charge: {charge}")
print(f"Surcharge: {surcharge}")
print(f"Final Bill: {final_bill}")
    