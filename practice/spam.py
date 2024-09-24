def repeat(word, n):
    print(word * n)

spam = "Spam, "

def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)

def last_three_lines():
    repeat(spam, 2)
    print("(Lovely Spam, Wonderful Spam!)")
    repeat(spam, 2)

def print_verse():
    first_two_lines()
    last_three_lines()


kmd = ""

while kmd != "exit":
    kmd = input("Liker du spam? j/n >> ")

    if kmd.lower() == "j":
        print_verse()

    elif kmd.lower() == "n":
        print(" D : ")

    else:
        print(" type 'exit' to exit program ")

