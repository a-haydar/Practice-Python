"""Write a password generator in Python. Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list."""
import random

def generate_password(length=8, strong=False):
    capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    smalls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '|', ':']
    password = list()
    
    password += random.sample(capitals, length//2)
    password += random.sample(smalls, length//2)
    if strong: password += random.sample(numbers, length//2)
    if strong: password += random.sample(specials, length//2)

    random.shuffle(password)
    return "".join(password[:length])

def main():
    strong = str(input("Do you need a strong password? [y/n]")) == "y"
    length = int(input("How long should the password be? "))

    print(generate_password(length, strong))

if __name__ == '__main__':
    main()
