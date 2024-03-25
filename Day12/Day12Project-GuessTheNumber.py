import random
from Day12GuessTheNumberArt import logo

def play_game(attempts):
    for i in range(attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {number}.")
            break
        attempts -= 1
    else:
        print(f"You've run out of guesses, you lose.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 an 100.")
number = random.randint(1, 100)
difficulty = input("Chose a difficulty level. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
    play_game(attempts)
elif difficulty == "hard":
    attempts = 5
    play_game(attempts)
