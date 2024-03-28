import random

listOfWords = ["apple","orange","grapes","pear"]
letterPicked = []
lives = 6

word = random.choice(listOfWords)

while True:
    letter = input("Choose a letter: ").lower()
    if letter in letterPicked:
        print("You ve already tried that")
        continue
    letterPicked.append(letter)
    if letter in word:
       print("You ve found a letter!")
    else:
       print("Nope,not in there")
       lives -= 1
        
    allLetters = True
    print()
    for i in word:
      if i in letterPicked:
        print(i,end="")
      else:
        print("_",end = "")
        allLetters = False
    print()
    
    if allLetters:
       print(f'You ve won with {lives} left!')
       
    if lives <= 0:
       print("You ve run out of lives :( ")
       break
    else:
       print(f"Only {lives} left!")
       
