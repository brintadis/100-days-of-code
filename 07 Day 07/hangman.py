import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo, stages


chosen_word = random.choice(word_list)
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ['_' for _ in chosen_word]
guessed_list = []

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in guessed_list:
        print("You've already guessed this letter.")
        continue
    else:
        guessed_list.append(guess)

    #Check guessed letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(f"Letter '{guess}' are not in guessed word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')

    print(*display)

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])