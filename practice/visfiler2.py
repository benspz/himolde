import os

#filer = os.listdir()
filer = [f"Item {i+1}" for i in range(50)] #testlist

antall = 0
nytt_antall = 0
while  antall < len(filer):
    print(filer[antall])
    antall += 1

    if antall == nytt_antall + 20:
        nytt_antall = antall
        svar = input(f"\nHar vist {antall} filer av {len(filer)}, vil du fortsette? (y/n) >> ")
        if svar.lower() != "y":
            break
    elif antall >= len(filer):
        print(f"\nHar vist alle {len(filer)} filer")
        break