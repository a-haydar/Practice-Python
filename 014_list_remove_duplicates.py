"""Write a program (function!) that takes a list and returns a new list that contains all the elements
 of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function."""

def remove_duplicates(lst):
    return list(set(lst))

def remove_duplicates_loop(lst):
    cleaned = []
    for i in lst:
        if i not in cleaned:
            cleaned.append(i)
    return cleaned

a = [5, 10, 15, 20, 25, 10, 44, 15, 20, 33]
print(remove_duplicates(a))
print(remove_duplicates_loop(a))
