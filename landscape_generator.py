import random
from termcolor import colored
from noise import pnoise2
from landscape_persistence import persist_to_file


def generate_land(cols=10, rows=10, noise_level = 10):
    total = cols * rows
    print(f"generate a landscape which is {cols} by {rows}")
    items = ["⛰️", "🌲", "🌲", "🏡", "🌲", "🌾","🌴","🌴","🌴","🏖️","🌊","🌊","🌊","🌊","🏖️","🌴","🌴","🌴","🏢","🌲","🌲","🌲"]
    seed = random.randint(0,100)
    land = ""

    for row in range(rows):
        for col in range(cols):
            n = round(pnoise2(row/rows, col/cols, base=seed, octaves=5) * noise_level) % len(items)
            land += items[n]

        land += "\n"
    
    return land
 
 

def ask_input_number(question):
    tries = 0
    while tries < 3:
        num = input(colored(f"{question} ", "green"))
        if question == "quit":
            quit()
        elif str.isnumeric(num):
            return int(num)
        else:
            print(colored("please enter a number!", "yellow"))
            tries += 1
    print(colored("you are not serious!!", "red"))
    quit()

if __name__ == "__main__":
    cols = ask_input_number("enter the number of columns: ")
    rows = ask_input_number("enter the number of rows: ")
    nl = ask_input_number("enter the noise level: ")

    land = generate_land(cols, rows, nl)
    persist_to_file(land)
