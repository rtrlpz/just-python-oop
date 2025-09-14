import random

guesses = []

computer_guess = random.randint(1, 70)

user_guess = int(input("Enter your guess 1 - 70: "))
guesses.append(user_guess)

while user_guess != computer_guess:
    if user_guess > computer_guess:
        print("Number is too high!")
    else:
        print("Number is too low")

    user_guess = int(input("Take another guess: "))
    guesses.append(user_guess)

else:
    print("Congrats!")
    print("Intents: %i" % len(guesses))
    print("These were your guesses:")
    print(guesses)
