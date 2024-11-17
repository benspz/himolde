def value_counts(word: str) -> dict:
    counter = dict()
    for letter in word:
        if letter in counter.keys():
            counter[letter] += 1
            continue
        counter[letter] = 1
    return counter


print(value_counts("brontosaurus"))

