# IBE152 H24 Oblig 5
# Skrevet av Benjamin Espeseth

import datetime
import os
# Brukt info fra: https://www.w3schools.com/python/module_os.asp
import time
# Brukt info fra: https://docs.python.org/3/library/time.html#time.perf_counter
import platform
import subprocess
import re

start = time.perf_counter()  # Setter startid for programmet

try:
    logg = open("mittskall.log", "x")  # Oppretter mittskall.log hvis den ikke eksisterer
except FileExistsError:
    pass


# les loggfil
def les_loggfil():
    lest = 0  # Initialiserer tellere
    godkjent = 0
    # https://chatgpt.com/share/671fd77c-12e8-8008-9e4b-f206b1eef3c4
    leser = open("mittskall.log", "r", encoding="ISO-8859-1")  # åpner loggfil i lesemodus
    for linje in leser:  # leser loggfil linje for linje og sjekker om det er gyldige
        lest += 1  # linjeteller
        # splitter hver linje på "," og fjerner whitespace fra høgre
        try:
            tidspunkt, kommando = linje.rstrip().split(",")
        except ValueError:  # ValueError hvis det er for mange input i loggfila på ei linje
            print(f"les_loggfil: feil antall felt på linje {lest}")
            continue
        try:
            print(f"les_loggfil: leste inn linje nr. {lest} :  {float(tidspunkt)} {str(kommando)}")
            godkjent += 1  # teller antall kommandoer uten error i loggfil
        except Exception as e:
            print(f"les_loggfil: feil type i tidspunkt/kommando på linje {lest}")
    print(f"Antall linjer lest inn er {lest} - Antall kommandoer er {godkjent}")
    leser.close()


les_loggfil()

print("Velkommen til Mitt Skall v0.05")
# Initialiserer variabler
kmd = ""
prompt = ">> "
forrige_kmd = ""
ant_kmd = 0
kmdlog = []
# Resett logg fil
# logg = open("mittskall.log", "w")
# logg.write("")
# logg.close()
# kjente_p_kmd = ["p", "pnyeste", "peldste", "pyramide"]    <- Metoden jeg brukte for p "n" før Regex

while kmd != "avslutt":
    kmd = input(prompt)
    ant_kmd += 1

    # Appender siste kommando til kmdlog
    kmdlog.append({
        "kommando": kmd,
        "tidspunkt": time.time(),
    })

    # Åpne/opprett loggfil og appender tidspunkt + kommando
    # https://www.w3schools.com/python/python_file_write.asp
    logg = open("mittskall.log", "a")
    logg.write(f"{time.time()}, {kmd}\n")
    logg.close()

    if kmd == "p" and forrige_kmd != "":
        kmd = forrige_kmd
        print("Utfører forrige kommando: " + kmd)
    forrige_kmd = kmd

    # https://pythex.org/  veldig kul regex tester
    # https://www.w3schools.com/python/python_regex.asp
    # https://chatgpt.com/share/671cb13c-8d28-8008-8498-dc7eaa8f527f
    match = re.search(r"^p\s*(-?\d+)$", kmd)
    if match:
        kmd = kmdlog[int(match.groups()[0])]["kommando"]
        print("Utfører kommando: " + kmd)
    forrige_kmd = kmd

    if kmd == "avslutt":
        print("Takk og farvel!")
        print(f"La til {ant_kmd} kommandoer i logfilen")

    elif kmd == "pnyeste":
        # https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
        n = input("Hvor mange kommandoer vil du se? >> ")
        print(f"Viser de {n} nyeste kommandoene")
        try:
            n = int(n)
        except TypeError:
            "Må være et tall!"
        index = len(kmdlog) - 2  # -2 her da 'pnyeste' også blir lagt til listen
        for linje in reversed(kmdlog[-n - 1:-1]):  # reverserer lista så vi kan iterere fra bunnen av
            print(f"{index} {linje['kommando']} : {linje['tidspunkt']}")
            index -= 1  # trekker fra 1 hver loop for å simulere liste index.

    elif kmd == "peldste":  # samme som 'pnyeste', men vi starter på toppen av lista
        n = input("Hvor mange kommandoer vil du se? >> ")
        print(f"Viser de {n} eldste kommandoene")
        try:
            n = int(n)
        except TypeError:
            "Må være et tall!"
        index = 0
        for linje in kmdlog[0:n]:
            print(f"{index} {linje['kommando']} : {linje['tidspunkt']}")
            index += 1

    elif kmd == "vistid":
        print("Dato og klokkeslett er:")
        tid = datetime.datetime.now()
        print(tid)

    elif kmd == "om":
        print("mittskall.py av Benjamin Espeseth v0.05 September 2024")

    elif kmd == "hjelp":
        print("Tilgjengelige kommandoer er: ")
        print("om, hjelp, vistid, vismappe, byttmappe, visfiler, vismiljø, peldste, pnyeste ")
        print("visbrukernavn, vispath, nyprompt, statiskboks, dynamiskboks, åpenboks, rombe, seil, pyramide, ")
        print("innafor, visfiler2, regnut, vismiljø2, vispath2, finnprogram, åpne, finn")
        print("\nFor å avslutte dette programmet, skriv 'avslutt' eller 'p' for å kjøre forrige kommando")

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
        totaltid = stop - start
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

    elif kmd == "innafor":  # Bruker Try Except Else istedenfor erTall() for å unngå error.
        def innafor(x, fra, til):  # erTall() blir overflødig da vi må caste input() før vi kaller på innafor()
            if fra <= til:  # Stigende
                return fra <= x <= til
            elif fra >= til:  # Fallende
                return til <= x <= fra


        try:
            x, fra, til = float(input("Velg tall >> ")), float(input("Velg tall >> ")), float(input("Velg tall >> "))
        except ValueError:
            print("Kun numeriske verdier støttet!")
        else:
            if innafor(x, fra, til):
                print("Innafor")
            else:
                print("Ikke innafor")

    elif kmd == "visfiler2":
        filer = os.listdir()
        # filer = [f"Item {i + 1}" for i in range(50)]
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # brukt for testing da jeg ikke har noen mapper med så mange filer : )
        antall = 0
        nytt_antall = 0
        while antall < len(filer):
            print(filer[antall])
            antall += 1
            if antall == nytt_antall + 20:  # Stopp etter 20 filer
                nytt_antall = antall  # Legg til 20, slik at neste gang stopper den på 40
                svar = input(f"\nHar vist {antall} filer av {len(filer)}, vil du fortsette? (y/n) >> ")
                if svar.lower() == "n":
                    break
            elif antall >= len(filer):
                print(f"\nHar vist alle {len(filer)} filer")
                break

    elif kmd == "regnut":
        uttrykk: str = input("Oppgi  uttrykk: >> ")
        try:
            print(eval(uttrykk))
        except NameError:
            print("Kun numeriske verdier støttet")

    elif kmd == "vismiljø2":
        for key in os.environ:
            print(f"{key}: {os.environ[key]}")  # Printer ut alle key:value par i os.environ

    elif kmd == "vispath2":
        # Bruker os.name for å sjekke om det er Windows eller Mac/Linux.
        for mappe in os.environ['PATH'].split(";" if os.name == 'nt' else ":"): print(mappe)

    elif kmd == "finnprogram":
        def finn_program(program):
            # Sjekker om platform er Windows eller Mac/Linux
            path = os.environ['PATH'].split(";" if os.name == 'nt' else ":")
            funnet = False
            for mappe in path:
                try:
                    if program in os.listdir(mappe):
                        print(f"{program} funnet i: {mappe}")
                        funnet = True
                        # break
                        # Brøyt loop originalt her da den alltid la til "fant ikke program" på slutten.
                        # Men endte opp med en "funnet" tag som sjekker om en eller flere har blitt funnet.
                except FileNotFoundError:
                    continue
            else:
                if not funnet: print("Fant ikke program")


        finn_program(input("Hvilket program leter du etter? >> "))

    elif kmd == "åpne":
        def åpne_fil(fil):
            # Bruker platform modulen her da os.name ikke differensierer mellom MacOS og Linux
            # https://chatgpt.com/share/be7f8a4d-db2b-4706-921e-287a30a15bf9
            # https://docs.python.org/3/library/subprocess.html
            try:
                if platform.system() == 'Windows':
                    os.startfile(fil)
                elif platform.system() == 'Darwin':  # MacOS
                    subprocess.run(["open", fil], check=True)
                else:  # Linux
                    subprocess.run(["xdg-open", fil], check=True)
            except Exception as e:
                print(f"Klarer ikke åpne fil: {e}")


        åpne_fil(input("Hvilken fil vil du åpne? >> "))

    elif kmd == "finn":
        def vistreff(søketekst, søkemappe):
            org_pos = os.getcwd()  # lagrer original posisjon
            os.chdir(søkemappe)  # cd inn i søkemappe i tilfelle bruker skriver relativ sti istedenfor absolutt.
            mapper = os.listdir()
            if søketekst in mapper:  # sjekk om fil er i nåværende mappe
                print(os.getcwd() + ("/" if os.name != "nt" else "\\") + søketekst)
                return
            for mappe in mapper:  # rekursivt sjekk alle undermapper.
                if os.path.isdir(mappe):
                    vistreff(søketekst, mappe)
            os.chdir(org_pos)


        # Ingen tilgang på jobbmaskina, men på den private Linux laptopen min så funker det i alle fall : )
        try:
            vistreff(input("Filnavn: >> "), input("Startmappe: >> "))
        except PermissionError:
            print("Ingen tilgang")


    else:
        print("Ukjent kommando")
        print("Skriv 'hjelp' for å se tilgjengelige kommandoer")
