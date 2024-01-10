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

print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice01 = input("The thick jungle surrounds you, alive with vibrant foliage and mysterious sounds. "
                 "You stand at a fork in the path, the choice between left and right stretching before you.").lower()
if choice01 == "left":
    choice02 = input("You forge ahead, the path narrowing as ancient trees loom overhead. "
                     "The air feels charged with anticipation. Ahead lies a murky river, cutting through the "
                     "jungle's heart. The sound of rushing water beckons. You will swim or wait? ").lower()
    if choice02 == "wait":
        choice03 = input("Opting to stay by the riverbank, time passes. Eventually, a clearing emerges,"
                         " revealing three ornate doors standing amidst overgrown vegetation. "
                         "Which door would you like to open? Red, Yellow or Blue. ").lower()
        if choice03 == "red":
            print("You cautiously open the red door, only to find it leads to a dead-end cavern, "
                  "filled with darkness. Game over.")
        elif choice03 == "yellow":
            print("The yellow door creaks open to reveal a glimmering chamber, "
                  "adorned with treasures and ancient artifacts. Congratulations, you've found the treasure! "
                  "Victory is yours! You Win.")
            print('''
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._''')
        elif choice03 == "blue":
            print("ush open the blue door, but an unexpected trap triggers, and the ground beneath you gives way. "
                  "Alas, this journey ends here. Game over.")
        else:
            print("Game Over.")
    else:
        print("The water seems tempting, but as you plunge in, the currents become relentless, "
              "pulling you deeper into unknown dangers. Unfortunately, this journey ends here. Game over.")
else:
    print("The path seems inviting, but as you venture further, the foliage thickens, blocking your way entirely. "
          "You're unable to proceed. Game over.")
