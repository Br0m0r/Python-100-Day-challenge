'''
print("-----------------------");
print ("Exam Grade Calculator")
print("-----------------------");
print("");
print ("Name of Exam: Algebra ")
print("");
MaxScore = float(input("Please insert the maximum possible score : "))
YourScore = float(input("Please insert your score : "))
PercentageScore  = (YourScore*100)/MaxScore
PercentageScore = round(PercentageScore,3);

if PercentageScore >= 90.00:
    print("You got",PercentageScore,"% which is  a A+")
elif PercentageScore < 90.00 and PercentageScore >= 80.00:
    print("You got",PercentageScore,"% which is  a A-")
elif PercentageScore < 80.00 and PercentageScore >= 70.00:
    print("You got",PercentageScore,"% which is  a B-")
elif PercentageScore < 70.00 and PercentageScore >= 60.00:
    print("You got",PercentageScore,"% which is  a C-")
elif PercentageScore < 60.00 and PercentageScore >= 50.00:
    print("You got",PercentageScore,"% which is  a D-")
elif PercentageScore < 50.00 and PercentageScore >= 40.00:
    print("You got",PercentageScore,"% which is  a U-")

'''

from getpass import getpass as input #this hides inputs
print("EPIC ROCK PAPER SCISSORS BATTLE");
print("");
print("Insert R : Rock || P : Paper || S : Scissors ")
print("");
P1 = input("Player 1! : Pick your move : ")
P2 = input("Player 2! : Pick your move : ")
if P1 == "R" and P2 == "P":
    print("Player 2 wins!")
elif P1 == "R" and P2 =="S":
    print("Player 1 wins!")
elif P1 == "P" and P2 == "R":
    print("Player 1 wins!")
elif P1 == "P" and P2 =="S":
    print("Player 2 wins!")
elif P1 == "S" and P2 == "R":
    print("Player 2 wins!")
elif P1 == "S" and P2 =="P":
    print("Player 1 wins!")
elif P1 == P2:
    print("Its a Draw!")
else :
    print("Invalid Input!")

    






