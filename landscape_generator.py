import random

def generate_land(cols=10,rows=10):
    total = cols * rows
    print(f"generate a landscape which is {cols} by {rows}")
    items = ["a","b","c","d","e","f"]
    for row in range(rows):
        strCol = ""
        for col in range(cols):
            strCol += random.choice(items)
        print(strCol)


def ask_input_number(question):
    tries = 0
    while tries < 3:
        num = input(question)
        if question == "quit":
            quit()
        elif str.isnumeric(num):
            return int(num)
        else:
            print("please enter a number!")
            tries+=1
    print("you are not serious!!")
    quit()


cols = ask_input_number("enter the number of columns: ")
rows = ask_input_number("enter the number of rows: ")

generate_land(cols,rows)