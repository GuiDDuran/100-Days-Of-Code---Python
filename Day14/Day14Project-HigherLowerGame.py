import random
import os
from Day14HigherLowerGameArt import logo, vs
from Day14HigherLowerGameData import data


def higherLowerGame():
    score = 0
    playing = True
    compare_a = random.choice(data)
    compare_b = random.choice(data)
    if compare_a == compare_b:
        compare_b = random.choice(data)

    print(logo)

    while playing:
        print(f"Compare A: {compare_a.get('name')}, a {compare_a.get('description')}, from {compare_a.get('country')}")
        print(vs)
        print(f"Against B: {compare_b.get('name')}, a {compare_b.get('description')}, from {compare_b.get('country')}")
        guess = input("Who has more followers? Type 'A' or 'B': ")

        if guess == 'A' and compare_a.get('follower_count') > compare_b.get('follower_count'):
            score += 1
            os.system('cls')
            print(logo)
            print(f"You are right! Current score: {score}.")
            compare_a = compare_a
            compare_b = random.choice(data)
            if compare_a == compare_b:
                compare_b = random.choice(data)
        elif guess == 'B' and compare_b.get('follower_count') > compare_a.get('follower_count'):
            score += 1
            os.system('cls')
            print(logo)
            print(f"You are right! Current score: {score}.")
            compare_a = compare_b
            compare_b = random.choice(data)
            if compare_a == compare_b:
                compare_b = random.choice(data)
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            playing = False


higherLowerGame()


