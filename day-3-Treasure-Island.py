print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

action1 = input("""Your boat just arrived to an island covered by dense jungle surrounded by tall mountains. 
The first thing you notice upon arrival is a small girl fishing. Would you like to approach her? Type Yes or No. \n""").lower()

if action1 == "no":
  print("You were shot by an arrow coming from the forest. Game over.")
elif action1 == "yes":
  action2 = input("""You approach the girl and ask her to show the way to the closest village to speak to the adult adventurers. 
  She gets suspicios and asks you what do you want from them. What do you answer? Type Treasure map or Food. \n""").lower()
  if action2 == "treasure map" or action2 == "treasuremap":
    print("The girl leads you to a village but you are brought in prison. Game over.")
  elif action2 == "food":
    print("You are broght to the village, invited for tribal dinner where you meet experienced pirate crew.")
    action3 = input("They propose you to join them. What do you say? Type Yes or No.  \n").lower()
    if action3 == "no":
      print("They discover that you search for their treasure and you are killed by pirates. Game over.")
    elif action3 == "yes":
      action4 = input("The pirates share with you the treasure map, you arrive to the treasure spot but there are three chests, which one do you choose? Choose Left, Central or Right. \n").lower()
      if action4 == "left": 
        print("You open the chest and get bitten by a snake. Game over.")
      elif action4 == "central":
        print("You find a letter from a different pirate crew that the treasure was already taken by them. Game over.")
      elif action4 == "right":
        print("You found the treasure! Congratulatons!")
      else:
        print("You chose the wrong key. Game over!")
    else: 
      print("They discover that you search for their treasure and you are killed by pirates. Game over.")
  else:
    print("The girl leads you to a village but you are brought in prison. Game over.")
else:
  print("You were shot by an arrow coming from the forest. Game over.")



