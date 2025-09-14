# --- IMPORTS --- #

import random
from time import sleep
import subprocess
import os

# --- BLOCK OF CODE --- #

# Clean the screen fuction depending on the OS
def clear_screen():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True   )

# Main game function
def play_game():

    # Ask the player if he wants to continue playing
    def continue_playing():
        continue_playing = input("Play again? (y/n): ").upper()
        if continue_playing  == "Y":
            clear_screen()
            play_game()
        elif continue_playing == "N":
            print("Thanks for playing!")

    # Return a random card from the deck
    def deal_cards():
        cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards_deck)

    # Calculate the score of the hand
    def calculate_score(list_of_cards):
        score = sum(list_of_cards)

        # Blackjack with 2 cards
        if score == 21 and len(list_of_cards) == 2:
            return 0

        # Adjust for Ace
        if 11 in list_of_cards and score > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)
        return sum(list_of_cards)

    # Compare the scores and determine who won the game
    def compare(user_score, computer_score):
        print("Wait for the result ... \n")
        sleep(3)

        print(f'Your final hand: {user_cards}, final score: {user_score}')
        print(f'House final hand: {computer_cards}, final score: {computer_score}\n')

        if user_score == 0 and computer_score == 0:
            print("Both have Blackjack! It's a draw! House wins by default.\n")
        elif user_score == computer_score:
            print("It's a draw!\n")
        elif computer_score == 0 or user_score > 21:
            print("House wins!\n")
        elif user_score == 0 or computer_score > 21 or user_score > computer_score:
            print("You win!\n")
        else:
            print("House wins!\n")
        
        # Ask the player if he wants to continue playing
        continue_playing()


    user_cards = [deal_cards(), deal_cards()]
    computer_cards = [deal_cards(), deal_cards()]

    print('Welcome to Blackjack!\n')
    sleep(1)
    print("Dealing cards...\n")
    sleep(2)
    print(f'Your cards: {user_cards}, current score: {calculate_score(user_cards)}')
    sleep(1)
    print(f"House cards: {computer_cards}")
    sleep(1)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Main game loop
    end_game = True
    
    while end_game:
        draw_card = input("\n Draw another card? (Y/N): ").upper()
        if draw_card == "Y":
            user_cards.append(deal_cards())
            print("Wait ... \n")
            sleep(1)
            print(f"These are your new cards: {user_cards}")
            user_score = calculate_score(user_cards)
            print(f"Your current score is: {user_score}")
        else:
            if computer_score < 17 and computer_score != 0:
                computer_cards.append(deal_cards())
                print("\nThe House is selecting a card, please wait...\n")
                sleep(3)
                print(f"These are the new House cards: {computer_cards}\n")
                computer_score = calculate_score(computer_cards)
            end_game = False

    compare(user_score, computer_score)

# --- MAIN PROGRAM --- #

play_game()




        