"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function."""

def list_ends(l):
    return [l[0], l[-1]]

def main():
    print(list_ends([2,4,5,6,7]))

if __name__ == '__main__':
    main()