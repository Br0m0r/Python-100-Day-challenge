# myDictionary = {"name" : "Ian","health" : 219,"strength": 199,"equipped":"Axe"}

# # for i in myDictionary:
# #     print (myDictionary[i])

# for name,value in myDictionary.items():
#     print(f'{name}: {value}')
#     if name == "strength":
#         if value>100:
#             print("Whoa,so strong!")
#         else:
#             print("Weak sauce dude!")
            


import os, time

Information = {"WebsiteName": None, "URL": None, "Description": None, "Rating": None}

print("Website Rating")
print()

while True:

  WebsiteName = input("Input the website name:").strip().capitalize()
  Information.update({"WebsiteName":WebsiteName})
  
  URL = input("Input the URL:").strip().capitalize()
  Information.update({"URL":URL})
  
  Description = input("Input your description:").strip().capitalize()
  Information.update({"Description":Description})
  
  Rating = input("Input a star rating out of 5:").strip().title()
  Information.update({"Rating":Rating})
  print()
  
  Information = {"WebsiteName": WebsiteName, "URL": URL, "Description": Description, "Rating": Rating}
  
  for name, value in Information.items():
      
    print(f"{name}: {value}")
      
    continue

  time.sleep(1)
  os.system("cls")
