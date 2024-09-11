print('''
*******************************************************************************
                                      CHEM  TREASURE                                                      .:
                                                      / )
                                                     ( (
                                                      \ )
      o                                             ._(/_.
       o                                            |___%|
     ___              ___  ___  ___  ___             | %|
     | |        ._____|_|__|_|__|_|__|_|_____.       | %|
     | |        |__________________________|%|       | %|
     |o|          | | |%|  | |  | |  |~| | |        .|_%|.
    .' '.         | | |%|  | |  |~|  |#| | |        | ()%|
   /  o  \        | | :%:  :~:  : :  :#: | |     .__|___%|__.
  :____o__:     ._|_|_."    "    "    "._|_|_.   |      ___%|_
  '._____.'     |___|%|                |___|%|   |_____(____  )
                                                           ( (
                                                            \ '._____.-
                                                             '._______.-
*******************************************************************************
''')
print("Welcome to Chem Island.")
print("Your mission is to find the Noble Gas.")
direction = input("You are at chem lab, Where do you want to go? \n  Type \"Left\" or \"Right\"").lower()
if direction == "Right" or direction == "right":
    print("**You broke the measuring cylinder ** (00) \n  ****GAME OVER******")
elif direction == "Left" or direction == "left":
    gloves = input("You found hand gloves, Do You want to wear it? \n Type yes or no").lower()
    if gloves == "yes":
        door = input("There are three coloured doors (Red, Yellow and Blue), "
                     "choose one \n red or yellow or blue?").lower()
        if door == "red" or door == "RED":
            print("**You found a burning Bunsen Burner**. \n *****GAME OVER*****")
        elif door == "yellow" or door == "Yellow":
           print("**You found sodium in water!** ****Blast****** \n *****GAME OVER*****")
        elif door == "blue" or door == "Blue":
           print("****Hurray! :) You found nobel gas **** \n **** YOU WON ****")
    elif gloves == "no" or "No":
        print("You burnt your hands \n *****GAME OVER*****")
    else:
        print("Type Error - Use small letters with correct spelling")
else:
    print("Type Error")





