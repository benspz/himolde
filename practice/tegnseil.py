def tegnseil(tegn, høyde):
    for x in range(int(høyde)):
        print(tegn * (x+1))

tegn = input("Velg tegn >> ")
høyde = input("Velg høyde >> ")
tegnseil(tegn, høyde)