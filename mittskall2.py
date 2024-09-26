# IBE152 H24 Oblig 2
# Skrevet av Benjamin Espeseth

import datetime
import os
#Brukt info fra: https://www.w3schools.com/python/module_os.asp
import time
#Brukt info fra: https://docs.python.org/3/library/time.html#time.perf_counter

start = time.perf_counter()

print("Velkommen til Mitt Skall v0.02")
kmd = ""
prompt = ">>"
forrige_kmd = ""
while kmd != "avslutt":
    kmd = input(prompt)

    if kmd == "p" and forrige_kmd != "":
        kmd = forrige_kmd
        print("Utfører forrige kommando: " + kmd)

    forrige_kmd = kmd

    if kmd == "avslutt":
        print("Takk og farvel!")

    elif kmd == "vistid":
        print("Dato og klokkeslett er:")
        tid = datetime.datetime.now()
        print(tid)

    elif kmd == "om":
        print("mittskall.py av Benjamin Espeseth v0.01 September 2024")

    elif kmd == "hjelp":
        print("Tilgjengelige kommandoer er: om, hjelp, vistid, vismappe, byttmappe, visfiler, vismiljø, "
                  "visbrukernavn, vispath, nyprompt, statiskboks, dynamiskboks, åpenboks, rombe, seil, og pyramide")
        print("For å avslutte dette programmet, skriv 'avslutt' eller 'p' for å kjøre forrige kommando")

    elif kmd == "vismappe":
        print(os.getcwd())

    elif kmd == "byttmappe":
        print("Nåværende mapper er:", os.getcwd())
        nymappe = input("Hvilken mappe vil du bytte til? >>")
        os.chdir(nymappe)
        print("Ny mappe er:", os.getcwd())

    elif kmd == "visfiler":
        print(os.listdir())

    elif kmd == "vismiljø":
        print(os.environ)

    elif kmd == "visbrukernavn":
        print(os.environ['USERNAME'])

    elif kmd == "vispath":
        print(os.environ['PATH'])

    elif kmd == "nyprompt":
        prompt = input("Oppgi ny prompt: ")
        print("Ny prompt er", prompt)

    elif kmd == "hvorlenge":
        stop = time.perf_counter()
        totaltid = stop-start
        timer = int(totaltid) // 3600
        minutter = int((totaltid % 3600) // 60)
        sekunder = int(totaltid % 60)
        print("Dette programmet har kjørt i", timer, "timer", minutter, "minutter og", sekunder, "sekunder.")

    elif kmd == "kakeplanlegger":
        gjester = input("Hvor mange gjester kommer? >> ")
        kakestykker = input("Hvor mange stykker er det i hver kake? >> ")
        kaker = (int(gjester) + int(kakestykker) - 1) // int(kakestykker)
        print("Du må lage", kaker, "kaker")
        # Fikk hjelp til matten fra:
        # https://www.reddit.com/r/C_Programming/comments/gqpuef/how_to_round_up_the_answer_of_an_integer_division/

    elif kmd == "dynamiskboks":
        n = input("Oppgi antall linjer/kolonner >> ")
        def tegnboks():
            x = input("Velg tegn >> ")
            for i in range(int(n)):
                print(str(x) * int(n))
        tegnboks()

    elif kmd == "statiskboks":
        for i in range(0, 4):
            print("*" * 4)

    elif kmd == "rombe":
        def rombe(tegn, høyde, bredde):
            for i in range(høyde):
                print(" " * i + (tegn * int(bredde)))
        tegn = input("Velg tegn >> ")
        høyde = input("Velg høyde >> ")
        bredde = input("Velg bredde >> ")
        rombe(tegn, int(høyde), int(bredde))

    elif kmd == "åpenboks":
        def åpenboks(tegn, høyde, bredde):
            print(tegn * int(bredde))
            for x in range(int(høyde) - 2):
                print(tegn + " " * (int(bredde) - 2) + tegn)
            print(tegn * int(bredde))
        tegn = input("Velg tegn >> ")
        høyde = input("Velg høyde >> ")
        bredde = input("Velg bredde >> ")
        åpenboks(tegn, int(høyde), int(bredde))

    elif kmd == "seil":
        def tegnseil(tegn, høyde):
            for x in range(int(høyde)):
                print(tegn * (x + 1))
        tegn = input("Velg tegn >> ")
        høyde = input("Velg høyde >> ")
        tegnseil(tegn, int(høyde))

    elif kmd == "pyramide":
        def pyramide(tegn, høyde):
            for x in range(int(høyde)):
                innrykk = (høyde - int(x)) / 2
                print(" " * int(innrykk) + (tegn * (x + 1)))
        tegn = input("Velg tegn >> ")
        høyde = input("Velg høyde >> ")
        pyramide(tegn, int(høyde))

    else:
        print("Ukjent kommando")
        print("Skriv 'hjelp' for å se tilgjengelige kommandoer")