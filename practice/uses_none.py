def uses_none(word: str, letters: str) -> bool:
    for letter in letters:
        if letter in word:
            return False
    return True

def uses_only(word: str, letters: str) -> bool:
    for letter in word:
        if not letter in letters:
            return False
    return True


def uses_all(word: str, letters: str) -> bool:
    for letter in letters:
        if not letter in word:
            return False
    return True

print(uses_all("banana", "ban")) # True
print(uses_all("apple", "api"))  # False
