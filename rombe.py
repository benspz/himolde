def rombe(tegn, høyde, bredde):
    for i in range(høyde):
        print(" " * i + (tegn * int(bredde)))

rombe("*", 5, 3)