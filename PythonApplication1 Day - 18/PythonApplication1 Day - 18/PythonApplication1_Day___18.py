import random,time,os
switch = True


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

def SetCharName():
    CharName = input("Name your Character: ")
    return CharName

def ChooseCharRace():
    switch = True
    while switch:
        CharType = input("Choose your Character Race: Human, Elf, Dwarf, Orc, Half-Giant  ")
        time.sleep(1)
        os.system("cls")
        if CharType not in ["Human", "Elf", "Dwarf", "Orc", "Half-Giant"]: #checked online and used (really helpful,not done yet on lessons)
            print("Choose a valid option")
            time.sleep(1)
            os.system("cls")
        else:
            return CharType

def CreateChar():
    print("-----------------")
    print("CHARACTER BUILDER")
    print("-----------------")

    CharName = SetCharName()
    CharType = ChooseCharRace()
    CharHP = RollHP()
    CharSTR = RollSTR()

    print(f'Name: {CharName}, Race: {CharType}')
    print(f'HP: {CharHP}')
    print(f'STR: {CharSTR}')
    print("May your name go down in legend...")
    time.sleep(1)
    print("")

    # Checked online how i could return multiple values(not yet done on lessons)
    return CharName, CharHP, CharSTR


def RollDice(side):
    return random.randint(1, side)

def Battle(char1, char1_hp, char1_str, char2, char2_hp, char2_str):
    while char1_hp > 0 and char2_hp > 0:
        char1_roll = RollDice(6)
        char2_roll = RollDice(6)

        if char1_roll > char2_roll:
            damage = char1_str - char2_str + 1
            char2_hp -= damage
            print(f"{char1} wins the round and deals {damage} damage! {char2} has {char2_hp} HP left.")
        elif char2_roll > char1_roll:
            damage = char2_str - char1_str + 1
            char1_hp -= damage
            print(f"{char2} wins the round and deals {damage} damage! {char1} has {char1_hp} HP left.")
        else:
            print("It's a tie this round, no damage dealt!")

        if char1_hp <= 0:
            print(f"{char2} wins the battle!")
            
        elif char2_hp <= 0:
            print(f"{char1} wins the battle!")
            

        time.sleep(1)  

#char create
char1_name, char1_hp, char1_str = CreateChar()
char2_name, char2_hp, char2_str = CreateChar()

#battle
Battle(char1_name, char1_hp, char1_str, char2_name, char2_hp, char2_str)

            









