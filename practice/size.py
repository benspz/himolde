import re

def string_size(text, size):
    word_list = text.split(" ")
    cleaned_word_list = [word.replace(".", "") for word in word_list]
    cleaned_word_list2 = [word.replace(",", "") for word in cleaned_word_list]
    cleaned_word_list3 = [word.replace("()", "") for word in cleaned_word_list2]
    for word in cleaned_word_list3:
        print(word)

def string_size_with_re(text, size) -> str:
    word_list = text.split()
    cleaned_list = [re.sub(r'[\W_]+', '', word) for word in word_list]
    for word in cleaned_list:
        if len(word) == int(size): 
            return word
    return ""
        

text = ("The Python String split() method splits all the words in a string separated by a specified separator."
    "This separator is a delimiter string, and can be a comma, full stop, space character or any other character "
    "used to separate strings. Usually, if multiple separators are grouped together, the method treats it as an empty "
    "string. But if the separator is not specified or is None, and the string consists of consecutive whitespaces, "
    "they are regarded as a single separator, and the result will contain no empty strings at the start or end if the "
    "string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just "
    "whitespace with a None separator results in an empty string.")

print(string_size_with_re(text, 10))