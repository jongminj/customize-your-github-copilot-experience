
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python to practice strings, loops, conditionals, and user input. The game will choose a hidden word and let the player guess letters before they run out of attempts.

## 📝 Tasks

### 🛠️ Build the Core Game

#### Description

Write a program that chooses a word from a predefined list and lets the player guess one letter at a time. Show the letters the player has guessed correctly and keep track of incorrect guesses.

#### Requirements

Completed program should:

- Choose a word randomly from a predefined list.
- Display each unguessed letter as an underscore and reveal correctly guessed letters in their positions.
- Ask the player for one letter per turn and accept uppercase or lowercase input.
- Keep track of incorrect guesses remaining, starting with 6 attempts.
- Continue asking for guesses until the player wins or runs out of attempts.

### 🛠️ Handle Results and Invalid Guesses

#### Description

Complete the game by checking each guess, handling invalid or repeated input, and reporting the result when the game ends.

#### Requirements

Completed program should:

- Reduce the remaining attempts after an incorrect letter guess.
- Not reduce attempts when the player enters something other than one letter or repeats a guessed letter.
- Display a win message when all letters in the hidden word have been guessed.
- Display a loss message and reveal the hidden word when no attempts remain.
- Show the current word progress and remaining attempts after each valid guess.
