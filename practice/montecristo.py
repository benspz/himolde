def reverse_sentence(sentence: str) -> str:
    word_list = sentence.split()
    sentence_reversed = " ".join(reversed(word_list))
    return sentence_reversed.capitalize()

def reverse_sentence2(sentence: str) -> str:
    return " ".join(reversed(sentence.split())).capitalize()

def total_length(word_list: list) -> None:
    count = 0
    for word in word_list:
        count += len(word)
    print(count)

sentence = "Reverse this sentence"
word_list = sentence.split()
#print(reverse_sentence(sentence))
#print(reverse_sentence2(sentence))
total_length(word_list)
