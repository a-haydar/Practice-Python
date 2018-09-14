"""Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order."""

def reverse(line):
    words = line.split()
    return " ".join(words[::-1])

line = str(input("Enter a line to reverse: "))
print(reverse(line))