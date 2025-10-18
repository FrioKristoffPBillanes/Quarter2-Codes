d = float(input("Enter distance in kilometers: "))
r = float(input("Enter rate per kilometer (₱): "))
df = round(float(d * r), 2)
print(f"Total Delivery Fee: ₱{df}") 
