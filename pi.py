#This script will find pi to the a user specified amount of decimals.
import math

decimal = ""
while decimal != "exit":

    decimal = input("How many decimal places do you want? (max = 15) >> ")

    pi = math.pi
    pi = str(pi)

    if decimal.isnumeric():
        if int(decimal) > 15:
            print("Too high!")

        elif int(decimal) < 0:
            print("Too low!")

        elif int(decimal) >= 0 and int(decimal) <= 15:
            decimal = int(decimal) + 2
            print(pi[0:decimal])

    else:
        print("meh")
