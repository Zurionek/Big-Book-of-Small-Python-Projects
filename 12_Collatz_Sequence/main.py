"""Collatz Sequence, by Al Sweigart
Generates numbers for the Collatz sequence, given a starting number
More about Collatz sequence under:
https://en.wikipedia.org/wiki/Collatz_conjecture
"""

import sys, time

print("""Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart

The Collatz sequence is a sequence of numbers produced from a starting number n, following 3 rules:
1)If n is even, the next number n is n / 2
2)If n is odd, the next number n is n * 3 + 1
3)If n is 1, stop. Otherwise repeat

It is generally thought, but so far not mathematically proven, that every starting number eventually terminates at 1.
""")

print('Enter a starting number (greater than 0) or QUIT:')
response = input("> ")

if not response.isdecimal() or response == '0':
    print("You must enter an integer greater than 0.")
    sys.exit()

n = int(response)
counter = 0
print(n, end = "", flush = True)
while n != 1:
    if n % 2 == 0: #if n is even
        n = n // 2
    else: #otherwise n is odd
        n = 3 * n + 1

    counter += 1
    print(", " + str(n), end = "", flush = True)
    time.sleep(0.1)
print()
print("Sequence takes {} steps before reaching out 1.".format(counter))