#Number Guessing Game
from art import logo
import random

print(logo)



guesses_left = 0
user_guess = 0
play_game = True
user_guesses = []

def start_game():
    correct_num = random.randint(1, 100)
    print("Guess a number between 1-100!")
    global guesses_left
    user_guesses = []
    while guesses_left >= 0:
      #  global user_guesses
        try:
            user_guess = int(input(f"You have guessed {user_guesses} so far. Guess a number! \nYou have {guesses_left} guesses left  "))
            if user_guess in range(1, 100):
                if user_guess in user_guesses:
                    print("You guessed that already!")
                else:
                    user_guesses.append(user_guess)
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
        except: 
            print(f"Try again, that was not a number.")
        




while play_game == True:
    user_play = input("Would you like to play a game? 'y' or 'n' ").lower()
    if user_play == 'n':
        play_game = False
        print("Goodbye")
    elif user_play == 'y':
        play_game = True
        difficulty = input("What difficulty would you like to play on? 'Easy: 10 lives' or 'Hard: 5 lives'? ").lower()
        if difficulty == "easy":
            guesses_left += 10
        elif difficulty == 'hard':
            guesses_left += 5
    else:
        play_game = False
        print("Invalid Input: Try again")

    if play_game == True:
        start_game()

        
        


