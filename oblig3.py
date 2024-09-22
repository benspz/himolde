#IBE152 H24 Oblig 3
#Skrevet av Benjamin Espeseth

#---------Deloppgave 1--------------------------------------------------------
def erTall(a, b, c):
    return isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))


def innafor(x, fra, til):
    if erTall(x, fra, til):
        if fra <= til:
            return fra <= x <= til
        elif fra >= til:
            return til <= x <= fra
    else:
        return False

x=50
print("Test av innafor()")
print(innafor(x,40,80))         # skal gi True i dette eksempelet
print(innafor(x,70,30))         # skal gi True i dette eksempelet
print(innafor(x,x,x))           # skal gi True uansett verdi av x
print(innafor(x, x-0.1, x-0.2))   # skal gi False uansett verdi av x
print(innafor(x, 2*x, 0.5*x))     # skal gi True uansett verdi av x
print(innafor("kake", 20, 70))



#---------Deloppgave 2--------------------------------------------------------

def countdownPar(n):
    if n == 0:
        print("Blastoff!")
    else:
        if n % 2 == 0:
            print(n)
            countdownPar(n-1)
        else:
            countdownPar(n-1)



def countdownOdde(n):
    if n == 0:
        print("Blastoff!")
    else:
        if n % 2 != 0:
            print(n)
            countdownOdde(n-1)
        else:
            countdownOdde(n-1)


def countdown2(n, parFlagg):
    if parFlagg:
        if n == 0:
            print("Blastoff!")
        else:
            if n % 2 == 0:
                print(n)
                countdown2(n-1, True)
            else:
                countdown2(n-1, True)
    else:
        if n == 0:
            print("Blastoff!")
        else:
            if n % 2 != 0:
                print(n)
                countdown2(n-1, False)
            else:
                countdown2(n-1, False)


print("\nTest av countdownOdde(6)")
countdownOdde(6)
print("\nTest av countdownPar(6)")
countdownPar(6)
print("\nTest av countdown2(10, True)")
countdown2(10, True)
print("\nTest av countdown2(3, False)")
countdown2(3, False)
