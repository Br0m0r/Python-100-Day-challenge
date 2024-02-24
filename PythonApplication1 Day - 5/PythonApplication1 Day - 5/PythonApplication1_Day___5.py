
'''
myScore = int ( input("Your score: "))
if myScore > 100000:
   print("winner!")
else:
   print("Try again :( ")



myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142:
   print("exactly!")
else :
   print("Try again :( ")
   '''
   

year = int(input("What year were you born? "))

if year >= 1946 and year <= 1964:
    generation = "Baby Boomer"
elif year >= 1965 and year <= 1980:
    generation = "Generation X"
elif year >= 1981 and year <= 1996:
    generation = "Millennial"
elif year >= 1997 and year <= 2012:
    generation = "Generation Z"
elif year >= 2013:
    generation = "Generation Alpha"
else:
    generation = "Unknown"


print("You belong to the", generation, "generation.")