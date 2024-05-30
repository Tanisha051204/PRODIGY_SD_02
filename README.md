Random Number Guessing Game


Overview


This program generates a random number and challenges the user to guess it. The program will prompt the user to input their guess, compare it to the generated number, and provide feedback on whether the guess is too high or too low. The game continues until the user correctly guesses the number, at which point it will display the number of attempts it took to win the game.


Features


Random number generation within a specified range.


User input for guessing the number.


Feedback on whether the guess is too high, too low, or correct.


Count of attempts taken to guess the number correctly.


Requirements


Python 3.x


Program Logic


The program generates a random number within a specified range (e.g., 1 to 100).


The user is prompted to guess the number.


The program compares the user's guess to the generated number:

If the guess is too high, the program outputs "Too high!" and prompts for another guess.


If the guess is too low, the program outputs "Too low!" and prompts for another guess.


If the guess is correct, the program outputs "Congratulations! You guessed the number in X attempts," where X is the number of attempts made.


The game continues until the correct number is guessed.
