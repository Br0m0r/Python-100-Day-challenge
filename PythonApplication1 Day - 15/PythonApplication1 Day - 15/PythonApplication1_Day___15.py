'''
def pinPicker(number):
    import random
    pin = ""
    for i in range(number):
        pin += str(random.randint(0,9))
    return pin
    
myPin = pinPicker(4)
print(myPin)
'''





def SetStats():
    import random
    add = ""
    for i in range(2):
        add += str(random.randint(1,2))
    return add
 
def rollHp(number):
    import random
    dice = random.randint(4,number)
    return dice

   
print("------------------------")
print("Character Stat Generator")
print("------------------------")

Name = input("Choose your character Name : ")
HP = (rollHp(6))* (rollHp(8))
STR = SetStats()
DEX = SetStats()
WIS = SetStats()
INT = SetStats()
AGI = SetStats()
LUC = SetStats()

print(f'{Name}"s stats are: ')
print(f'HP: {HP}')
print(f'STR: {STR}')
print(f'DEX: {DEX}')
print(f'WIS: {WIS}')
print(f'INT: {INT}')
print(f'AGI: {AGI}')
print(f'LUC: {LUC}')


