while True:
    age = input("Please enter your age >> ")

    if age.lower() == "quit":
        break
    elif int(age) <= 3:
        print("\nThe ticket is free!")

    elif int(age) > 3 and int(age) <= 12:
        print("\nThe ticket costs $10")

    elif int(age) > 12:
        print("\nThe ticket costs $15")
