import os
import time
from Day09SecretAuctionArt import logo

print(logo)
print("Welcome to The Secret Auction!")

bids = {}
bidding_finished = False

def highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What's your name? ")
    bid_price = int(input("What's your bid? $"))
    bids[name] = bid_price
    option = input("There's other player who want to bid? ")
    if option == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif option == "yes":
        time.sleep(1)
        os.system('cls')
