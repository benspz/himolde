sandwich_orders = ["Pastrami","Reuben", "Club", "Pastrami",  "Tuna", "Pastrami", "BLT"]
finished_sandwiches = []


print("The restaurant has run out of pastrami")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nMaking {sandwich}")

    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
