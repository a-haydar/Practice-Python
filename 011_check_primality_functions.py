"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you."""

import math

def is_prime(number):
    K = math.ceil(math.sqrt(number))+1
    return not is_divisible_by_any(number,generate_primes(K))

def generate_primes(max):
    primes = [2]
    for i in range(3,max):
        if not is_divisible_by_any(i,primes):
                primes.append(i)
    return primes


def is_divisible_by_any(number, divisors):
    """Return True if a number is divisible by any divisor in a list, False otherwise"""
    for x in divisors:
        if number % x == 0: return True
    return False

def main():
    number = int(input("Enter a number to check: "))
    print(f"{number} is "+ ("prime" if is_prime(number) else "not prime"))

if __name__ == '__main__':
    main()
