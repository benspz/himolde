def pyramide(tegn, høyde):
    for x in range(int(høyde)):
        innrykk = høyde - int(x)
        print(" " * innrykk + (tegn * (x + 1)))


def tegnpyramide(tegn, høyde):
    for x in range(høyde):
        for i in range(-abs(høyde)):
            innrykk = i
            if x % 2 == 0:
                innrykk -= 1

            print(" " * abs(innrykk) + str(tegn) * (x+1))



tegnpyramide("*", 10)
