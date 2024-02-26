'''Unconventional way of doing this,but i do it just to showcase a bit more


print("How many seconds are there in a year? Lets find out!")
print("")

year = input("Count for leap year or not? Answer 'yes' for leap year or ' not' ")
seconds = int(input("Insert seconds "))
minutes = int(input("Insert minutes "))
hours = int(input("insert hours"))
monthDaysEven = int(input("insert how many  days in a month when days are even "))
monthDaysOdd =  int(input("insert how many days in a month when days are odd "))
FebruaryLeap = int(input("insert days of February if its a leap year! "))
FebruaryNotLeap = int(input("insert days of February if its not a leap year! "))

if year == "yes" or "Yes":
     holdDays = ((monthDaysEven*4) + (monthDaysOdd*7) + FebruaryLeap)
     SecondsInYear1 = (seconds * minutes * hours * holdDays)
     print("There are",SecondsInYear1,"seconds in a leap year!")
    
elif year == "not" or "Not":
     
     holdDays2= ((monthDaysEven*4) + (monthDaysOdd*7) + FebruaryNotLeap)   
     SecondsInYear2 =(seconds * minutes * hours * holdDays2)
     print("There are",SecondsInYear2,"seconds in a non leap year!")
else:
    input("Please enter valid input")   
    



Else what i can do is : '''

'''
print("How many seconds are there in a year? Let's find out!")
print("")
year = input("Count for leap year or not? Answer 'yes' for leap year or 'not': ")
SecondsInMinute = 60
MinutesInHour = 60
HoursInDay = 24
DaysInLeapYear = 366
DaysInNonLeapYear = 365

if year == "yes" or "Yes":
    SecondsInYear1 = SecondsInMinute * MinutesInHour * HoursInDay * DaysInLeapYear;
    print("There are",SecondsInYear1,"in a leap year!")
elif year == "Not" or "not":
    SecondsInYear2 = SecondsInMinute * MinutesInHour * HoursInDay * DaysInNonLeapYear;
    print("There are",SecondsInYear2,"in a non leap year!")
else :
    print("Please enter a valid input")

'''

'''correct the mistakes'''
'''
print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?)
ans1 = ("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope
ans2 = input("Which lesson number is this?")
if(ans2>12):
print("We're not quite that far yet")
else:
  print("We've gone well past that!")
elif(ans2==12):
  print("That's right!")
'''

print("100 Days of Code QUIZ")

print("")

print("How many can you answer correctly?")

ans1 = input("What language are we writing in?")

if ans1 == "python":
  print("Correct")
else:
  print("Nope")
  
ans2 = int(input("Which lesson number is this?"))

if ans2 > 12 :
   print("We're not quite that far yet")
elif ans2 < 12:
  print("We've gone well past that!")
else :
  print("That's right!")



    
