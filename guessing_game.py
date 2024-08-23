"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
# import random to gen random number for game and sys for program exit
import random
import sys

# create list to store users and their scores for printing to console
# see line 61-63
high_score = [5]

def header():
# Welcome the player with a bold header
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("*-*-*-*Welcome to the Number Guessing Game*-*-*-*")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
# simply explain the rules of the game    
    print("Guess the correct number in as few tries as possible!\nIf it takes more than 5 tries, you lose!\nGood luck!")
    return header

       
# create the start_game func with core game logic to be called upon start of game & again if user wishes to replay    
def start_game():
    print(f"Score to Beat: {min(high_score)}")
    
    # count users guesses, set to 0 initially
    attempts = 0
    
    # generate random number 1 - 10 for user to guess
    winning_num = random.randint(1, 10)
    
    # create user_guess var and set to None so the variables are not equal when the loop begins
    # https://www.youtube.com/watch?app=desktop&v=pZoDH6aU7ws
    user_guess = None
    # check the users guess vs the winning num
    while user_guess != winning_num and attempts < 5:
        # prompt user for guess and store as var and integer
        while user_guess != int:
            try:
                user_guess = int(input("Guess a # from 1 - 10: "))
                if 1 <= user_guess <= 10:
                    break
                else:
                    print("Enter a number between 1 - 10.")
            except ValueError:
                print("You can not use letters, special characters or number with decimals.")
                
               
        # if guess is lower than winning num print feedback to screen, count the guess
        if user_guess < winning_num:
            attempts +=1
            print("Too low, try again.")
# when the user reaches the max attempts user is prompted to play again
# set max attempts at 5 to safeguard the high_score list at program start and is preferable to setting the high_score 
# initially to a high number because a user could simply enter the same wrong number however many times is 
# neccessary to break the program theoretically
            if attempts >= 5:
                print("You're out of guesses! You lose!")
                while True:
                    play_again = input("Play again? y/n: ").lower()
# if user selects 'y' the game begins again minus the header since we have the same user
                    if play_again == "y":
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        start_game()
# if user selects no they are given a thannk you message and game ends                   
                    elif play_again == "n":
                        sys.exit("Thanks for playing!")
                    else:
                        print("You must choose 'y' or 'n'.")

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
                while True:
                    play_again = input("Play again? y/n: ").lower()
                    if play_again == "y":
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        start_game()
                    elif play_again == "n":
                        sys.exit("Thanks for playing!")
                        
                        






header()
start_game()