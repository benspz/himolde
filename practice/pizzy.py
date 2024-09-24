while True:
    prompt = "What topping would you like to add?"
    prompt += "\n(Type 'quit' to end the program) >> "
    topping = input(prompt)
    if topping.lower() == "quit":
        break
    else:
        print(f"\nI will add {topping} to the pizza")

