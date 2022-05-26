#   import time, os & sys packages
import time
import os
import sys

#   Message title
print("\n__________ 🎮MY CRYPTO QUIZ GAME🎮 ___________\n")
print("Play while you earn🤑.....\n\n")

#   Function to delay program(game) for 3 seconds
time.sleep(3)

#   Requests player name
player = input("\nEnter your player name here🧑: \n")

#   Error Message on null input
while player.lower() == '':
    print("ERROR: INVALID INPUT😕")
    player = input()

    if player.lower() != '':
        break

#   Requests player input to begin the game
play = input("\nHey there "+ player +"!, would you like to proceed🔐?(y/n) \n")

#   Declaring default variable
user_input = 'False'

#   Modify variable if condition is true
if play.lower() == 'n' or play.lower() == 'y' or play.lower() == 'no' or play.lower() == 'yes':
    user_input = 'True'

#   Error message if condition is not met
while user_input != 'True':   
    print("ERROR: INVALID INPUT😕")
    play = input()

    if play.lower() == 'n' or play.lower() == 'y' or play.lower() == 'no' or play.lower() == 'yes':
        break

#   Condition to exit or continue the game
if play.lower() == 'n' or play.lower() == 'no':
    print("\nWe're sad to see you leave ", player,". \nGoodBye🥺.")
    os.system("pause")
    quit()  
else:
    print("\nAlright",player +", we wish you good fortunes.\nENJOY!! 🤗")

#   Function to delay program(game) for 3 seconds
time.sleep(2)

#   Wait message for player
print("\nYour quiz will start in a few seconds...")

#   Function to delay program(game) for 4 seconds
time.sleep(4)

#   Initializing variables
score = 0
coins = 0.00000
count = 0

#   Instruction message on how to play the game
print("\n\n\n***** Kindly answer the questions provided with its corresponding alphabets😊.*****\n\n")

#   Function to delay program(game) for 3 seconds
time.sleep(3)

#   Game questions & answers stored in an array
questions = [ ' What does CPU stand for?\n a. Center Process Uniform    b. Central Procure Unit     c. Central Processing Unit     d. Central Processing Unix',
            ' Who founded Apple Computer\n a. Stephen Fry     b. Bill Gates      c. Stephen Hawking    d. Steve Jobs',
            ' Where is the CPU located?\n a. On the motherboard    b. On the fatherboard      c. On the auntieboard      d. On the ROM',
            ' Which device is used for clicking?\n a. Mice      b. Mouse    c. Monitor      d. Mic',
            ' Which of the following devices displays the desktop?\n a. VRA     b. Photocronic lense    c. LCD      d. Headphone',
            ' How many computer languages are in use?\n a. 2000     b. 5000     c. 50   d. 20',
            ' Who was responsible for some of the earliest, widely influential development of military rockets?\n a. Elon Musk      b. William Congreve       c. Hermann Oberth     d. Robert Hutchings Goddard',
            ' What does fiber optic cable resemble, in terms of size?\n a. Pipeline     b. Bamboo      c. Telephone wire        d. Human hair',
            ' When did the compact disc first appear on the market?\n a. 1982     b. 1992     c. 1955     d. 1989',
            ' Who invented flexible photographic film?\n a. Leonardo da Vinci     b. Linda Eastman    c. George Eastman     d. Louis Daguerre'
            ]

answers = [ 'c',
            'd',
            'a',
            'b',
            'c',
            'a',
            'b',
            'd',
            'a',
            'c'
        ]

#   Condition to display question and process answers simultaneously
for answer in questions:
    print(questions[count])
    answer = input()

    if answer.lower() == answers[count]:
        print("✔️\n")
        score += 1
        coins += 0.00252
    else:
        print("❌\n")

    count += 1

    if count == 5:
        print("\n\n\n*** FINAL ROUND ***\n\n")
        time.sleep(4)


#   Message displaying score sheet & coins earned
print("\n\n\nSCORE SHEET:")   
print("You had " + str(score)+ " answer(s) right and " + str(count - score) + " wrong(s).")
print("You scored " + str((score/10) *100))
print("\n\nREWARD:")
if score != 0 or coins != 0:
    print("Congratulations " + player + "🎉. You earned " + str(coins) + "BTC")
else:
    print("Too bad " + player +"😓, better luck next time.")

#   Function to pause the program(game)
os.system("pause")