"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""
import random

guess_count = 0
guess_correct = 0
num = random.randint(1,9) #initial
while True:
    guess = input("Your guess: ")
    if guess == "exit":
        break
    guess = int(guess)
    guess_count += 1
    
    if guess == num:
        print("Correct!")
        guess_correct += 1
        num = random.randint(1,9)
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")
    
print(f"You guessed {guess_count} times, of which, {guess_correct} were correct!")

