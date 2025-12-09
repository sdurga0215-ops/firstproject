import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        break
