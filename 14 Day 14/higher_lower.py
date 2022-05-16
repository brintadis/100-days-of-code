import random
import os
from art import logo, vs
from game_data import data


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def side_format(side):
    return f"{side['name']}, {['a', 'an'][any([side['description'].lower().startswith(i) for i in 'aeioyu'])]} " \
           f"{side['description']}, from {side['country']}"


def check_guess(guess, a_side, b_side):
    if a_side['follower_count'] > b_side['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
game_on = True
print(logo)
b = random.choice(data)

while game_on:
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)

    print(f"Compare A: {side_format(a)}")
    print(vs)
    print(f"Against B: {side_format(b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    clearConsole()
    print(logo)
    if check_guess(guess, a, b):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False