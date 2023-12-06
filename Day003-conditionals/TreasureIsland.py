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
    _________|___________| ;`-.o`"=._; ." ` '`."_ . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/______/
    *******************************************************************************
    ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
left_right = input("You\'re arriving to an intersection and you have to options: turn 'left' or turn 'right'. \nWhich one do you choose? : ").lower()
if left_right == "right":
    print("Fall into a hole...\nGAME OVER.")
else:
    swim_wait = input("You are walking on the road and find a big river. \nWhat do you want to do: 'wait' or 'swim'? : ").lower()
    if swim_wait == "swim":
        print("Attacked by trout...\nGAME OVER.")
    else:
        red_yellow_blue = input("Someone pass with a little ship and invite you to cross the river with him, then you walk on a new road and at one point you find three doors flagged as 'Red', 'Yellow' or 'Blue'... Which one would you choose to open? ").lower()
        if red_yellow_blue == "red":
            print("Burned by fire...\nGAME OVER.")
        elif red_yellow_blue == "blue":
            print("Eaten by beasts...\nGAME OVER.")
        elif red_yellow_blue == "yellow":
            print("YOU WIN !!!")
        else:
            print("GAME OVER.")