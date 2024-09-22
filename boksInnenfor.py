def boksInnenfor(a, b, c, x, y, z):
    measurements = [a, b, c]     # https://www.w3schools.com/python/python_lists_sort.asp
    measurements.sort(reverse=True)
    if measurements[0] <= x and measurements[1] <= y and measurements[2] <= z:
        return True
    else:
        return False

print(boksInnenfor(90, 20, 50, 100, 30, 20))   # This should be False
print(boksInnenfor(10, 20, 30, 30, 20, 10))   # This should be True