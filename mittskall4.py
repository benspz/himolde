# IBE152 H24 Oblig 4
# Skrevet av Benjamin Espeseth

import sys
import os
import datetime
import time
import platform
import subprocess

#------init_variabler-------------------------------------------------------------

start = time.perf_counter()
kommando = ""
forrige_kmd = ""
prompt = ">> "

#------Function definitions--------------------------------------------------

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
    for mappe in os.environ['PATH'].split(";" if os.name == 'nt' else ":"): print(mappe)

def finnprogram():
    # Sjekker om platform er Windows eller Mac/Linux
    path = os.environ['PATH'].split(";" if os.name == 'nt' else ":")
    app = input("Velg app: >> ")
    for dir in path:
        try:
            if app in os.listdir(dir):
                print(f"{app} funnet i: {dir}")
                break
        except FileNotFoundError:
            continue
    else:
        print("Fant ikke program")

def åpne():
    fil = input("Velg fil: >> ")
    try:
        if platform.system() == 'Windows':
            os.startfile(fil)
        elif platform.system() == 'Darwin':
            subprocess.run(["open", fil], check=True)
        else:
            subprocess.run(["xdg-open", fil], check=True)
    except Exception as e:
        print(f"Klarer ikke åpne fil: {e}")

def finn():
    søketekst = input("Hva leter du etter? >> ")
    søkemappe = input("Hvor skal søket starte? >> ")
    org_pos = os.getcwd()
    os.chdir(søkemappe)
    mapper = os.listdir()
    if søketekst in mapper:
        print(os.getcwd() + "/" + søketekst)
        return
    for mappe in mapper:
        if os.path.isdir(mappe):
            finn()
    os.chdir(org_pos)

def avslutt():
    sys.exit()

def kjør_forrige():
    if kommando == "p" and forrige_kmd != "":
        kommando = forrige_kmd
        print("Utfører forrige kommando: " + kommando)


#------Kommandoer-------------------------------------------------------------

kommandoer = {
    "vistid": vistid,
    "vismappe": vismappe,
    "visfiler": visfiler,
    "byttmappe": byttmappe,
    "hvorlenge": hvorlenge,
    "om": om,
    "vismiljø": vismiljø,
    "visbrukernavn": visbrukernavn,
    "vispath": vispath,
    "nyprompt": nyprompt,
    "kakeplanleger": kakeplanlegger,
    "statiskboks": statiskboks,
    "dynamiskboks": dynamiskboks,
    "åpenboks": åpenboks,
    "rombe": rombe,
    "seil": seil,
    "pyramide": pyramide,
    "innafor": innafor,
    "visfiler2": visfiler2,
    "regnut": regnut,
    "finn": finn,
    "finnprogram": finnprogram,
    "vismiljø2": vismiljø2,
    "vispath2": vispath2,
    "åpne": åpne,
    "hjelp": hjelp,
    "avslutt": avslutt,
    "p": kjør_forrige,
}

#------Hovedprogram---------------------------------------------------------------

if __name__ == "__main__":
    while True:
        kommando = input(prompt)
        if kommando in kommandoer:
            kommandoer[kommando]()
        forrige_kmd = kommando