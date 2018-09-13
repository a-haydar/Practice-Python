"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

while True:
    num = input("Enter a number:")
    num = int(num)
    if num < 0:
        break
    if num % 2 == 0:
        print(f"{num} is even", end="")
        if num % 4 == 0:
            print(" and is divisible by 4")
        else:
            print()
    else:
        print(f"{num} is odd")
