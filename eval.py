uttrykk :str = input("Oppgi  uttrykk: >> ")

try: print(eval(uttrykk))
except NameError: print("Kun numeriske verdier støttet")