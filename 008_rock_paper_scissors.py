"""Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""

#it is probably better to assign numbers to hands and check the difference
while True:
    hand_1 = input("Player 1, your hand is? ")
    hand_2 = input("Player 2, your hand is? ")
    if hand_1 == hand_2:
        print("It is a tie!")
    if (hand_1 == "rock" and hand_2 == "scissors") or (hand_1 == "scissors" and hand_2 == "paper") or (hand_1 == "paper" and hand_2 == "rock"):
        print("Player 1 wins")
    else:
        print("Player 2 wins")
    play_again = input("Play again? [y/n] :")
    if play_again[0] == "n":
        break