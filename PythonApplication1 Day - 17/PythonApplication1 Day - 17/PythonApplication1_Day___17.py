


#HP  ((6 sided dice * 12 sided dice) / 2 ) + 10
#STR ((6 sided dice * 8 sided dice) / 2 )  + 10

# Character Builder
  
# Name your Legend :
# Gorlock the destroyer

# Character Type(Human,Elf,Wizard,Orc)
# Orc

# Gorlock the destroyer
# Health : 13
# Strength : 18

# May your name go down in legend

# Again?:
# Yes


import random,time,os
from telnetlib import DO
switch = True
switch2 = True
switch3 = True

#i can alse make a function 'rollDice' to just input how many sides i want

def RollDice(side):
    result = random.randint(1,side)
    return result


def RollHP():
    a = random.randint(1,6)
    b = random.randint(1,12)
    HP = int((a * b)/2)
    return HP + 10;

def RollSTR():
    a = random.randint(1,6)
    b = random.randint(1,8)
    STR = int((a*b)/2)
    return STR + 12




while switch:
    print("-----------------")
    print("CHARACTER BUILDER")
    print("-----------------")
    print("")
    time.sleep(1)
    os.system("cls")
    CharName = input("Name your legend: ")
    time.sleep(1)
    os.system("cls")
    while switch2:
        CharType = input("Choose your Character Race : Human, Elf, Dwarf, Orc, Half-Giant  ")
        time.sleep(1)
        os.system("cls")
        if CharType != "Human" and CharType != "Elf" and CharType != "Dwarf" and CharType != "Orc" and CharType != "Half-Giant":
            print("Choose a valid option")
            time.sleep(1)
            os.system("cls")
        else:
            switch2 = False
            break
    time.sleep(1)
    os.system("cls")   
    print(f'Name : {CharName},  {CharType}')
    print(f'HP : {RollHP()}')
    print(f'STR : {RollSTR()}')
    time.sleep(1)
    print("May your name go down in legend...")
    time.sleep(1)
    print("")
    while True:
        choose = input("Want to create a new character? (Y/N): ")
        if choose == "Y":
            time.sleep(1)
            os.system("cls")
            break
        elif choose == "N":
            print("Thank you for playing!")
            exit()
        else:
            print("Pick a valid option")
        
    
    
    
# (GPT CREATED)  :

# import random
# import time
# import os

# def roll_stat(die1, die2, bonus):
#     return int((random.randint(1, die1) * random.randint(1, die2)) / 2) + bonus

# def choose_character_type():
#     valid_types = ["Human", "Elf", "Dwarf", "Orc", "Half-Giant"]
#     while True:
#         char_type = input("Choose your Character Race (Human, Elf, Dwarf, Orc, Half-Giant): ")
#         if char_type in valid_types:
#             return char_type
#         print("Choose a valid option")

# def create_character():
#     os.system("cls")
#     char_name = input("Name your legend: ")
#     char_type = choose_character_type()
#     hp = roll_stat(6, 12, 10)
#     str = roll_stat(6, 8, 12)

#     print(f"\nName: {char_name}, {char_type}\nHP: {hp}\nSTR: {str}")
#     print("May your name go down in legend...\n")

# def main():
#     while True:
#         create_character()
#         if input("Want to create a new character? (Y/N): ").lower() == 'n':
#             print("Thank you for playing!")
#             break

# if __name__ == "__main__":
#     print("CHARACTER BUILDER")
#     main()




