responses = {}


while True:
    name = input("\nWhat is you name? >> ")
    destination = input("Where would you like to go? >> ")

    responses[name] = destination

    repeat = input("\nWould the next person like to respond? (y/n) >> ")
    if repeat.lower() == "n" or "no":
        break

print("\n--- Poll Results ---")
for name, destination in responses.items():
    print(f"\n{name} would like to go to {destination}")
