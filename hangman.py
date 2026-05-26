import random

# List of predefined words
words = ["python", "computer", "program", "student", "science"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print(f"You have {max_attempts} incorrect guesses.\n")

# Game loop
while wrong_guesses < max_attempts:

    # Display current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        remaining = max_attempts - wrong_guesses
        print("❌ Wrong guess!")
        print("Attempts remaining:", remaining)

# If player loses
if wrong_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing Hangman!")