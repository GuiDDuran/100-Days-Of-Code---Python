import random
from Day11BlackjackArt import logo
import os
import time


def deal_card():  # The function is used to pick a random card from the list cards.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_sum(cards):  # It's responsible for check the blackjack's possibilities, the ace value and sum the score.
    if sum(cards) == 21 and len(cards) == 2:  # Check if there is a blackjack, because a hand with only 2 cards and a
        # score of 21 is a blackjack.
        return 0
    if 11 in cards and sum(cards) > 21:  # Check if the ace will count as an 11 or 1, to the player don't lose.
        cards.remove(11)  # It removes the current value of the ace and then add the new value (1).
        cards.append(1)
    return sum(cards)


def compare(sum_player, sum_computer):  # Responsible for saying who is the winner, according to the conditions.
    if sum_player == sum_computer:
        return "It's a draw :)"
    elif sum_computer == 0:
        return "You lose! the opponent has a blackjack."
    elif sum_player == 0:
        return "You win with a blackjack!"
    elif sum_player > 21:
        return "You went over, you lose."
    elif sum_computer > 21:
        return "The opponent went over, you win."
    elif sum_player > sum_computer:
        return "Your score is greater than you opponent, you win!"
    else:
        return "You lose"


def play_game():  # It's the main function, where the game happens.
    print(logo)  # The logo is imported from the art.

    player_cards = []  # The empty lists were created to add the random cards from the list.
    computer_cards = []
    is_game_over = False

    for i in range(2):  # This loop is responsible for add two random numbers in each list.
        player_cards.append(deal_card())  # By doing that, it's added a random number in each empty list.
        computer_cards.append(deal_card())

    while not is_game_over:  # The loop keeps running until the game is in the end.
        sum_player = calculate_sum(player_cards)  # Here we attribute the sum of the cards for each player.
        sum_computer = calculate_sum(computer_cards)
        print(f"Your cards are {player_cards}, and your current score is: {sum_player}.")
        print(f"The computer's first card is: {computer_cards[0]}")

        if sum_player == 0 or sum_computer == 0 or sum_player > 21:  # If any of these conditions happen, the game ends.
            is_game_over = True
        else:
            should_continue = input("Type 'yes' to get one more card, or type 'no' to pass: ")  # If the game
            # continues, we are going to ask the player if it wants other card.
            if should_continue == "yes":
                player_cards.append(deal_card())  # If the player don't want to play one more time, the game ends.
            else:
                is_game_over = True

    while sum_computer < 17 and sum_computer != 0:  # The loop continues to add cards into the computer cards list
        # until it's less than 17 and there's not a blackjack.
        computer_cards.append(deal_card())
        sum_computer = calculate_sum(computer_cards)
    print(f"Your final hand is : {player_cards}, and your final score: {sum_player}")
    print(f"The computer's final hand is: {computer_cards}, and it's final score is: {sum_computer}")
    print(compare(sum_player, sum_computer))  # Here the compare function is called to see who is the winner.


while input("Type 'yes' to play a game of Blackjack or 'no': ") == "yes":  # It asks the user if it wants to play the
    # game.
    time.sleep(1)  # Both the functions were to clean the console.
    os.system('cls')
    play_game()
