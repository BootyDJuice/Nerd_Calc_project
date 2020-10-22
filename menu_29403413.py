# Author: Semen Mordovin
# ID: 29403413
# Start Date: 04/04/2019
# Last Modification Date: 11/04/2019

""" Importing math library to use ia square operation in our Nerd Score formula
"""

import math

""" Assigning main variables for our program. Printing the introduction for us
er and creating main menu representation. Creating list for table representation
of Nerd Classes """

print("Welcome to the Nerd Score!")
menu = ("\tCHOOSE THE ACTION:\n\tTo enter your Fandom Score press 1\n\t"
        "To enter your Hobbies Score press 2\n\tTo enter Number of Sports playe"
        "d ""press 3\n\tTo calculate your Nerd Score press 4\n\tTo print Nerd R"
        "ating ""of students press 5\n\tTo exit Nerd Score press 0")
fandom_score = 0
hobbies_input = 0
sport_played = 0
nerd_score = 0
option_to_choose = 0
nerd_table_list = [["0", "Nerdlite", "0"], ["1", "Nerdling", "1"],
                   ["10", "Nerdlinger", "2"],
                   ["100", "Nerd", "3"], ["500", "Nerdington", "4"],
                   ["1000", "Nerdometa", "5"], ["2000", "Nerd Supreme", "6"]]

""" Creating main loop for menu to pop up each time till user decide to quit. 
Asking user for input to choose from possible option of our program. Main idea 
is to use while loop for the purpose of constant request from user. Using
if/elif/else conditional statements to implement prescribed solutions and 
outcomes"""

while fandom_score == 0 or nerd_score == 0 or sport_played == 0:
    print(menu)
    option_to_choose = int(input("Your choice: "))
    if option_to_choose == 1:  # First Option is - Fandom Score
        fandom_score = int(input("\tWHAT IS YOUR FANDOM SCORE?: "))
        while fandom_score == 0 or fandom_score < 0:  # Prescribed conditions
            fandom_score = int(input("Fandom Score can not be less or equal 0! "
                                     "Try again: "))  # Error message
        if fandom_score != 0 or fandom_score > 0:
            print("Your Fandom Score is", fandom_score)  # Right choice of score
    elif option_to_choose == 2:  # Second Option - is Hobbies of a Nerd
        hobbies_input = int(input("\tHOW MUCH HOBBIES YOU HAVE?: "))
        while hobbies_input % 4 != 0:  # Prescribed conditions
            hobbies_input = int(input("You typed wrong Hobbies number! "
                                      "Try again:"))
        if hobbies_input % 4 == 0:
            print("Your Hobbies Score number is:", hobbies_input)  # Right Pick
        if hobbies_input == 0:
            warning = str(input("If choose 0 hobbies you will get 0 Nerd Score!"
                                ": Y/N"))  # Warning for user that choosing
            # 0 Hobbies lead to 0 Nerd Score outcome
            if warning == "Y":
                continue
    elif option_to_choose == 3:  # Third option - Number of Sports
        sport_played = int(input("ENTER NUMBER OF SPORTS YOU PLAY: "))
        while sport_played <= 0:  # Prescribed conditions
            sport_played = int(input("Number of sport played can not be "
                                     "less than zero! Try again: "))
        if sport_played > 0:
                print("Number of sport you play is:", sport_played)  # Correct
                # Pick
    elif option_to_choose == 4:  # Fourth Choice - Nerd Score Calculation, while
        # loops used to show user what numbers missing for calculations, if you
        # have all numbers it computes your Nerd Score
        while fandom_score == 0:
            print("YOU MISSING FANDOM SCORE! "
                  "Fill your Fandom Score in!")
            break
        while hobbies_input == 0:
            print("YOU MISSING NUMBER OF HOBBIES OR TYPED 0! "
                  "You can not use Nerd Score calculation "
                  "if number of hobbies is 0! Fill with right number!")
            break
        while sport_played == 0:
            print("YOU MISSING NUMBER OF SPORTS! Fill number of sports you play"
                  "")
            break
        if fandom_score and hobbies_input and sport_played != 0:
            # Representation of a main formula to compute Nerd Score, when right
            # conditions are met
            x = fandom_score
            y = hobbies_input
            z = sport_played
            a = y ** 2
            b = a * 42
            c = z + 1
            square = b // c
            nerd_score = x * (math.sqrt(square))
            print(nerd_score)
    elif option_to_choose == 5:  # This Option is created to Display Table of
        # Nerd Classes of people
        print("This is division for your nerd classes: ")
        print("| Score | Classification| Output|")
        for item in nerd_table_list:  # Using for loop to represent our table in
            # human readable form
            print("|", item[0], " " * (4 - len(item[0])), "|",
                  item[1], " " * (12 - len(item[1])), "|",
                  item[2], " " * (4 - len(item[2])), "|")
    elif option_to_choose == 0:  # As an assumption I have choose the option
        # just to quit Nerd Score if user do not feel like to continue :)
        exit_option = str(input("Are you sure you want to quit Nerd Score?: Y/N"
                                ""))
        if exit_option == "Y":
            print("Goodbye!")
            break
        elif exit_option == "N":
            continue
        else:  # This statements works if something except possible variants was
            # typed
            print("You typed wrong button, try again")

    else:
        print("YOU TYPED A WRONG OPTION, TRY AGAIN")

    """This while loop is used to give an opportunity for user to recalculate 
    his or ger score if needed when it is already calculated or quit program"""

    while nerd_score != 0:
        answer = str(input("You got your score, you want to keep this one "
                           "or to calculate it again?: Y/N"))
        if answer == "Y":
            nerd_score = 0
        elif answer == "N":
            print("Your final Nerd Score", nerd_score, "!")
            break
        else:
            print("You typed wrong button, try again")
