import random

def number_guesser(min, max):
    low = min
    high = max
    feedback = ""

    while feedback != 'c':
        guess = (min, max) // 2

        feedback = input(f"Is {guess} too high (h), too low (l), or correct?").lower()

        if feedback == 'h':
            max = guess - 1
        elif feedback == 'l':
            min = guess + 1

    print(f"This is the right number, {guess}.")

min = 1
max = 300

print("Please choose a number in your head that is between 1 and 300.  Let me try and guess it")
number_guesser(min, max)



