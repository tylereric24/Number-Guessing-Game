#Number Guessing Game
from art import logo
import random

print(logo)


correct_num = random.randint(1, 100)
guesses_left = 0
play_game = True

def start_game():
    global guesses_left
    while guesses_left >= 0:
        user_guess = int(input("Guess a number! "))
        if user_guess != correct_num and guesses_left == 1:
            print(f"Game over! The number was {correct_num}")
            break
        elif user_guess > correct_num:
            print("Lower")
            guesses_left -= 1
        elif user_guess < correct_num:
            print("Higher!")
            guesses_left -= 1
        elif user_guess == correct_num:
            print("You got it, you win!")
            break
        




while play_game == True:
    user_play = input("Would you like to play a game? ").lower()
    if user_play == "no":
        play_game = False
        print("Goodbye")
    elif user_play == 'yes':
        difficulty = input("What difficulty would you like to play on? 'Easy' or 'Hard'? ").lower()
        if difficulty == "easy":
            guesses_left += 10
        elif difficulty == 'hard':
            guesses_left += 5
    start_game()
        


