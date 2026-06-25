import random

# List of predefined words
words = ["python", "apple", "computer", "coding", "program"]

# Randomly select a word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")

while incorrect_guesses < max_guesses:

    # Display current word progress
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
        print("Please enter a single alphabet letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct Guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Attempts:", max_guesses - incorrect_guesses)

# Game Over
if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The word was:", word)