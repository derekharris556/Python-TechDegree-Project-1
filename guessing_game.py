"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
# import random to gen random number for game
import random
# import sys to exit the game
import sys

# create list to store users and their scores for printing to console
# see line 61-63
high_score = [9]

def header():
# Welcome the player with a bold header
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("*-*-*-*Welcome to the Number Guessing Game*-*-*-*")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
# simply explain the rules of the game    
    print("Guess the correct number in as few tries as possible!\nIf it takes more than 9 tries, you lose!\nGood luck!")
    return header
    
# create the start_game func with core game logic to be called upon start of game & again if user wishes to replay    
def start_game():
    print(f"Score to Beat: {min(high_score)}")
    # get user name, ensure valid name using characters is entered, not blanks
    #https://stackoverflow.com/questions/51764409/how-to-prevent-user-from-inputting-spaces-nothing-in-python
    while True:
        try:
            user = input("Enter your username: ")
            if len(user.strip()) >= 1:
                break
        except:
            print("Please enter a valid user name.")
        return user    

    # count users guesses, set to 0 initially
    attempts = 0
    # generate random number 1 - 10 for user to guess
    winning_num = random.randint(1, 10)
    # create user_guess var and set to None so the variables are not equal when the loop begins
    # https://www.youtube.com/watch?app=desktop&v=pZoDH6aU7ws
    user_guess = None
    # check the users guess vs the winning num
    while user_guess != winning_num and attempts < 9:
        # prompt user for guess and store as var and integer
        while True:
            try:
                user_guess = int(input("Guess a # from 1 - 10: "))
                if 1 <= user_guess <= 10:
                    break
            except ValueError:
                print("Using your numpad, enter # from 1 - 10.")
            
            print(f"Sorry {user}! You lose! You're out of guesses!")    
        # if guess is lower than winning num print feedback to screen, count the guess
        if user_guess < winning_num:
            attempts +=1
            print("Too low, try again.")
# when the user reaches the max attempts the game will end and display a message
# setting the max attempts at 9 safeguards the high_score list and is preferable to setting the high_score initially to a high number
# because a user could simply enter the same wrong number however many times is neccessary to break the program
            if attempts >= 9:
                print(f"Sorry {user}! You're out of guesses! You lose!")
                sys.exit  
        # check if guess is higher than winning num and print feedback to sreen, count the guess 
        elif user_guess > winning_num:
            attempts += 1
            print("Too high, try again!")
        # if guess is equal to winning num, count the guess, tell user they are correct and give total number of guesses    
        else:
            attempts +=1
            print(f"Correct! It took you {attempts} guesses!")
            if attempts < high_score[0]:
                high_score.append(attempts)
            
        # prompt the user to play again, accepting 1 of 2 valid choices
            while True:
                    play_again = input("Play again? y or n: ").lower()
        # if user does wish to play again, reset attempts & user_guess & regen new random number for player to guess    
                    if play_again == "y":
                        start_game()
        # is user doesnt wish to play, break loop and print thank you message                
                    elif play_again == "n":
                        print(f"Thanks for playing {user}!")
                        sys.exit
        #            
                    else:
                        print("Please make a valid selection.")





header()
start_game()