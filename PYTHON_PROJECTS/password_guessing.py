import random

easy_words = ["ant", "apple", "money", "cat", "ball", "bubble"]
medium_words = ["elephant", "hammer", "monkey", "planet", "laptop", "gitam"]
hard_words = ["python", "diamond", "helicopter", "umbrella", "mountain", "computer"]

print("Welcome to password guessing game!!")
print("Choose your difficulty level: easy, medium, hard")

level = input("Enter your difficulty level: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice, defaulting to easy level.")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the correct password:")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f" Congratulations! You guessed it in {attempts} attempts.")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:", hint)

print("Game over")
