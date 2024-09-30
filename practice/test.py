def boksInnenfor(a, b, c, x, y, z):

    if a >= b and a >= c:
        største = a
        if b >= c:
            mellomste = b
            minste = c
        else:
            mellomste = c
            minste = b
    elif b >= a and b >= c:
        største = b
        if a >= c:
            mellomste = a
            minste = c
        else:
            mellomste = c
            minste = a
    else:
        største = c
        if a >= b:
            mellomste = a
            minste = b
        else:
            mellomste = b
            minste = a

    return største <= x and mellomste <= y and minste <= z



print(boksInnenfor(90, 20, 50, 100, 30, 20))  # False
print(boksInnenfor(10, 20, 30, 30, 20, 10))  # True
