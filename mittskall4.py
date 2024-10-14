# IBE152 H24 Oblig 4
# Skrevet av Benjamin Espeseth

import os
import datetime
import time
import platform
import subprocess

from visfiler2 import nytt_antall

start = time.perf_counter()

#------Function definitions---------------------------------------------

def vistid():
    tid = datetime.datetime.now()
    print(f"Dato og klokkeslett er: {tid}")

def om():
    print("Mitt Skall v.0.04, Oktober 2024 av Benjamin Espeseth")

def hjelp():
    pass

def vismappe():
    print("os.getcwd()")

def byttmappe():
    print(f"Nåværende mappe er: {os.getcwd()}")
    nymappe = input("Hvilken mappe vil du bytte til? >> ")
    os.chdir(nymappe)
    print(f"Ny mappe er {nymappe}")

def visfiler():
    print(os.listdir())

def vismiljø():
    print(os.environ)

def visbrukernavn():
    print(os.environ['USERNAME'])

def vispath():
    print(os.environ['PATH'])

def nyprompt():
    prompt = input("Oppgi ny prompt: ")
    print("Ny prompt er", prompt)

def hvorlenge():
    stop = time.perf_counter()
    totaltid = stop - start
    timer = int(totaltid) // 3600
    minutter = int((totaltid % 3600) // 60)
    sekunder = int(totaltid % 60)
    print("Dette programmet har kjørt i", timer, "timer", minutter, "minutter og", sekunder, "sekunder.")

def kakeplanlegger():
    gjester = input("Hvor mange gjester kommer? >> ")
    kakestykker = input("Hvor mange stykker er det i hver kake? >> ")
    kaker = (int(gjester) + int(kakestykker) - 1) // int(kakestykker)
    print("Du må lage", kaker, "kaker")
    # Fikk hjelp til matten fra:
    # https://www.reddit.com/r/C_Programming/comments/gqpuef/how_to_round_up_the_answer_of_an_integer_division/

def statiskboks():
    for i in range(0, 4):
        print("*" * 4)

def dynamiskboks():
    n = input("Oppgi antall linjer/kolonner >> ")
    x = input("Velg tegn >> ")
    for i in range(int(n)):
        print(str(x)*int(n))

def åpenboks(tegn, høyde, bredde):
    print(tegn * int(bredde))
    for x in range(int(høyde) - 2):
        print(tegn + " " * (int(bredde) - 2) + tegn)
    print(tegn * int(bredde))

def rombe(tegn, høyde, bredde):
    for i in range(høyde):
        print(" " * i + (tegn * int(bredde)))

def seil(tegn, høyde):
    for x in range(int(høyde)):
        print(tegn * (x + 1))

def pyramide(tegn, høyde):
    for x in range(int(høyde)):
        innrykk = (høyde - int(x)) / 2
        print(" " * int(innrykk) + (tegn * (x + 1)))

def erTall(a, b, c):
    return isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))

def innafor(x, fra, til):
    if erTall(x, fra, til):
        if fra <= til:  # Stigende
            return fra <= x <= til
        elif fra >= til:  # Fallende
            return til <= x <= fra
    else:
        return False

def visfiler2():
    filer = os.listdir()
    antall = 0
    nytt_antall = 0
    while antall < len(filer):
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

def regnut():
    uttrykk: str = input("Oppgi  uttrykk: >> ")
    try: print(eval(uttrykk))
    except NameError: print("Kun numeriske verdier støttet")

def vismiljø2():
    for key in os.environ:
        print(f"{key}: {os.environ[key]}")

def vispath2():
    for mappe in os.environ['PATH'].split(":"): print(mappe)

def finnprogram():
    pass

def åpne():
    pass

def finn():
    pass