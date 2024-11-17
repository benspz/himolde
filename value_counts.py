def value_counts(word: str) -> dict:
    counter = dict()
    for letter in word:
        counter[letter] = counter.get(letter, 0) + 1
    return counter


def has_duplicates(word: str) -> bool:
    for value in value_counts(word).values():
        if value > 1:
            return True
    return False

print(value_counts("brontosaurus"))
print(has_duplicates("brontosaurus"))
print(has_duplicates("unpredictably"))
