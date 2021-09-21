
#Number guessing game for understanding Random number generation in Python
#import random package
import random

#initialize empty attempts list
attempts_list = []

#define the entire scope of the game

def game():
    start_game = input("Start game? (Enter Yes/No) ")
    random_number = int(random.randint(1,1000))

    #init attempt counter
    attempts = -1
    
    #while loop for game functionality
    while start_game == "Yes":
        try:
            guess = input("Pick a number between 1 and 1000: ")

            #if statement for remaining within bounds of random
            if (int(guess) < 1 or int(guess) > 1000):
                raise ValueError("Please guess within the range of 1 and 1000")
            
            #if statement for victory condition
            if int(guess) == random_number:
                print("Congrats, you guessed the number")
                attempts += 1
                attempts_list.append(attempts)
                print("you made {} attempts".format(attempts))
                replay = input("Play again? (Yes/No) ")
                attempts = 0
                random_number = int(random.randint(1,1000))
                
                #if statement for replaying
                if start_game == "No":
                    print("Better luck next time")
                    break
            elif (int(guess) > int(random_number)):
                print("Lower")
                attempts += 1
            elif (int(guess) < random_number):
                print("Higher")
                attempts += 1
            if (int(attempts) > 13):
                print("You took too many attempts")
                attempts += 1
                attempts_list.append(attempts)
                print("you made {} attempts".format(attempts))
                replay = input("Play again? (Yes/No) ")
                attempts = 0
                random_number = int(random.randint(1,1000))

                if start_game == "No":
                    print("Better luck next time")
                    break

        except ValueError as err:
            print("That value is invalid")
            print("({})".format(err))
    else:
        print("goodbye")


game()