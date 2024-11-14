def is_triangle(a, b, c) -> bool:
    if a + b > c:
        if a + c > b:
            if b + c > a:
                return True
    return False

print(is_triangle(50, 50, 50))
    
    