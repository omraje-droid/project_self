
import random

words = ["apple", "tiger", "mango", "robot", "python"]

word = random.choice(words)
guessed = ""
chances = 6

print("Welcome to Hangman Game!")

while chances > 0:
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    if all(letter in guessed for letter in word):
        print("You won!")
        break

    guess = input("Guess one letter: ").lower()

    if guess in word:
        guessed = guessed + guess
        print("Correct guess!")
    else:
        chances = chances - 1
        print("Wrong guess!")
        print("Chances left:", chances)

if chances == 0:
    print("You lost!")
    print("The word was:", word)
