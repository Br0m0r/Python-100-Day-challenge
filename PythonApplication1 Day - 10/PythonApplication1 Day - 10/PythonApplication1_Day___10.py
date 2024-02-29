'''
while True:
    print("You are in a corridor,do you go left or right?")
    direction = input("> ")
    if direction == "left":
        print("You have fallen to your death")
        break
    elif direction == "right":
        continue
    else:
        print("Ahh!You re a genius,you ve won!")
        exit()
print("The game is over,you ve failed!")        
'''


#from getpass import getpass as input #this hides inputs
print("EPIC ROCK PAPER SCISSORS BATTLE")
print("")
print("Insert R : Rock || P : Paper || S : Scissors ")
print("")

P1V = 0
P2V = 0

while P2V < 3 and P1V < 3:
    P1 = input("Player 1! : Pick your move : ")
    P2 = input("Player 2! : Pick your move : ")

    if P1 == "R" and P2 == "P":
        print("Player 2 wins!")
        P2V += 1
    elif P1 == "R" and P2 =="S":
        print("Player 1 wins!")
        P1V += 1
    elif P1 == "P" and P2 == "R":
        print("Player 1 wins!")
        P1V += 1
    elif P1 == "P" and P2 =="S":
        print("Player 2 wins!")
        P2V += 1
    elif P1 == "S" and P2 == "R":
        print("Player 2 wins!")
        P2V += 1
    elif P1 == "S" and P2 =="P":
        print("Player 1 wins!")
        P1V += 1
    elif P1 == P2:
        print("Its a Draw!")
    else :
        print("Invalid Input!")
    print("Current Score - Player 1:",P1V,"Player 2:",P2V,"")

if P2V == 3:
    print("And the winner is Player numbahh 2")
    
if P1V == 3:
    print("And the winner is Player numbahh 1")
        


