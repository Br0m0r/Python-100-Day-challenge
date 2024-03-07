
# import os

# for i in range(1,1000):
#     print(i)
#     os.system("cls")


# import os
# import time

# print("Welcome")
# print("to")
# print("Jurassic Park")

# time.sleep(1)
# os.system("cls")

# username = input("Username: ")




# import os
# import time

# from playsound import playsound

# # Play your MP3 file  
# #Use Raw Strings: Prefix your string with an 'r' to make it a raw string.
# #In raw strings, backslashes are treated as literal characters and not as escape characters.


# playsound(r'D:\Downloads\Sounds_Music\Nah ah ah!.mp3')           #\n would do the thingy it does

# #OR

# # playsound('D:\\Downloads\\Sounds_Music\\Nah ah ah!.mp3')



import os
import time
from playsound import playsound

print("-------------------")
print("MyPOD Music Player")
print("-------------------")
print("")
switch = True
while switch:
    print("Type 'Play' to play song")
    print("Type 'Exit' to exit the player")
    print("--------------------------")
    UserInput = input("")
    time.sleep(1)
    if UserInput == "Play":
       playsound('D:\\Downloads\\Sounds_Music\\Nah ah ah!.mp3')
       time.sleep(1)
       os.system("cls")
    elif UserInput == "Please Play":
       playsound('D:\\Downloads\\Sounds_Music\\rick_roll.mp3')
       time.sleep(1)
       os.system("cls")
    elif UserInput == "Exit":
       print("Thank you for using MyPod Music Player,bye bye")
       switch = False
       time.sleep(1)
       os.system("cls")
    else:
       print("Wrong Input")
       time.sleep(1)
       os.system("cls")
print("Bye Bye!")       
       
           
    