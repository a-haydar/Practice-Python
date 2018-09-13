"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""
string = input("Enter a string: ")
print("String is" + (" a " if string[len(string)::-1] == string else " not a ") + "palindrome")
