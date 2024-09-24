def åpenboks(tegn, høyde, bredde):
    print(tegn * int(bredde))
    for x in range(int(høyde) - 2):
        print(tegn + " " * (int(bredde) - 2) + tegn)
    print(tegn * int(bredde))


åpenboks("*", 10, 7)