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
# see line 51-53
high_score = [5]

def header():
# Welcome the player with a bold header
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("*-*-*-*Welcome to the Number Guessing Game*-*-*-*")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
# simply explain the rules of the game    
    print("Guess the correct number in as few tries as possible!\nIf it takes more than 5 tries, you lose!")
    return header

def play_again():
# prompt the user to play again, accepting 1 of 2 valid choices
            while True:
                try:
                    play_again = input("Play again? y or n: ").lower()
        # if user does wish to play again, reset attempts & user_guess & regen new random number for player to guess    
                    if play_again == "y":
                        return True
        # is user doesnt wish to play, break loop and print thank you message                
                    elif play_again == "n":
                        return False
                    else:
                        print("Enter 'y' or 'n'. No other inputs will be accepted.") 
                except:
                    print("Please make a valid selection. Either 'y' or 'n'.")
    
# create the start_game func with core game logic to be called upon start of game & again if user wishes to replay    
def start_game():
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"Score to Beat: {min(high_score)}")

    # count users guesses, set to 0 initially
    attempts = 0
    # generate random number 1 - 10 for user to guess
    winning_num = random.randint(1, 10)
    # create user_guess var and set to None so the variables are not equal when the loop begins
    # https://www.youtube.com/watch?app=desktop&v=pZoDH6aU7ws
    user_guess = None
    # check the users guess vs the winning num
    while user_guess != winning_num and attempts <= 5:
        # prompt user for guess and store as var and integer
        while True:
            try:
                user_guess = int(input("Guess a # from 1 - 10: "))
                if 1 <= user_guess <= 10:
                    break
                elif user_guess <= 0:
                    print("That number is out of range.")
                elif user_guess >= 11:
                    print("That number is out of range")
            except ValueError:
                print("You can only use whole numbers.\nNo decimals, negatives, letters ,special characters or blanks.")
                
        # if guess is lower than winning num print feedback to screen, count the guess
        if user_guess < winning_num:
            attempts +=1
            print("Too low!")
# when the user reaches the max attempts the game will end and display a message
# setting the max attempts at 5 to match initial the high_score and is preferable to setting the high_score to a high number
# because a user could simply enter the same wrong number however many times is neccessary to break the program
            if attempts >= 5:
                print("You're out of guesses! You lose!")
                if play_again():
                    start_game()
                else:
                    sys.exit("Thanks for playing!")    
        # check if guess is higher than winning num and print feedback to sreen, count the guess 
        elif user_guess > winning_num:
            attempts += 1
            print("Too high!")
        # if guess is equal to winning num, count the guess, tell user they are correct and give total number of guesses    
        else:
            attempts +=1
            print(f"Correct! It took you {attempts} guesses!")
            if attempts < min(high_score):
                high_score.append(attempts)
            if play_again():
                start_game()
            else:
                sys.exit("Thanks for playing!")    






header()
start_game()