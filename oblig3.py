# IBE152 H24 Oblig 3
# Skrevet av Benjamin Espeseth

# ---------Deloppgave 1--------------------------------------------------------
def erTall(a, b, c):
    return isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))


def innafor(x, fra, til):
    if erTall(x, fra, til):
        if fra <= til:  #Stigende
            return fra <= x <= til
        elif fra >= til:  #Fallende
            return til <= x <= fra
    else:
        return False


x = 50
print("Test av innafor()")
print(innafor(x, 40, 80))  # skal gi True i dette eksempelet
print(innafor(x, 70, 30))  # skal gi True i dette eksempelet
print(innafor(x, x, x))  # skal gi True uansett verdi av x
print(innafor(x, x - 0.1, x - 0.2))  # skal gi False uansett verdi av x
print(innafor(x, 2 * x, 0.5 * x))  # skal gi True uansett verdi av x
print(innafor("kake", 20, 70))


# ---------Deloppgave 2--------------------------------------------------------

def countdown(n):
    if n == 0:
        print("Blastoff!")
    elif n > 0:   #Positiv
        print(n)
        countdown(n - 1)
    else:        #Negativ
        print(n)
        countdown(n + 1)


def countdownPar(n):
    if n == 0:
        print("Blastoff!")
    elif n > 0:     #Positiv
        if n % 2 == 0:
            print(n)
            countdownPar(n - 1)
        else:
            countdownPar(n - 1)
    else:           #Negativ
        if n % 2 == 0:
            print(n)
            countdownPar(n + 1)
        else:
            countdownPar(n + 1)

def countdownOdde(n):
    if n == 0:
        print("Blastoff!")
    elif n > 0:    #Positiv
        if n % 2 != 0:
            print(n)
            countdownOdde(n - 1)
        else:
            countdownOdde(n - 1)
    else:        #Negativ
        if n % 2 != 0:    #Negativ
            print(n)
            countdownOdde(n + 1)
        else:
            countdownOdde(n + 1)


def countdown2(n, parFlagg):
    if n == 0:
        print("Blastoff!")
    elif parFlagg:   #Partall
        if n > 0:       #Positiv
            if n % 2 == 0:
                print(n)
                countdown2(n - 1, True)
            else:
                countdown2(n - 1, True)
        else:           #Negativ
            if n % 2 == 0:
                print(n)
                countdown2(n + 1, True)
            else:
                countdown2(n + 1, True)
    else:            #Oddetall
        if n > 0:       #Positiv
            if n % 2 != 0:
                print(n)
                countdown2(n - 1, False)
            else:
                countdown2(n - 1, False)
        else:           #Negativ
            if n % 2 != 0:
                print(n)
                countdown2(n + 1, False)
            else:
                countdown2(n + 1, False)


print("\nTest av countdown(6)")
countdown(6)
print("\nTest av countdownPar(6)")
countdownPar(6)
print("\nTest av countdownOdde(6)")
countdownOdde(6)
print("\nTest av countdown2(6, True)")
countdown2(6, True)
print("\nTest av countdown2(6, False)")
countdown2(6, False)


# ---------Deloppgave 3--------------------------------------------------------

def boksInnenfor(a, b, c, x, y, z):
    measurements = [a, b, c]  # https://www.w3schools.com/python/python_lists_sort.asp
    measurements.sort(reverse=True)
    if measurements[0] <= x and measurements[1] <= y and measurements[2] <= z:
        return True
    else:
        return False


print("\nTest av boksInnenfor(90, 20, 50, 100, 30, 20)")
print(boksInnenfor(90, 20, 50, 100, 30, 20))  # This should be False
print("\nTest av boksInnenfor(10, 20, 30, 30, 20, 10)")
print(boksInnenfor(10, 20, 30, 30, 20, 10))  # This should be True
