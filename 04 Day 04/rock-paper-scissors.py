import random


def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    player_chose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
    my_list = [rock, paper, scissors]
    computer_chose = random.randint(0, 2)


    if player_chose < 0 or player_chose >= 3:
        print('You typed and invalid number, you lose!')
    else:
        print(my_list[player_chose])
        print('Computer chose:')
        print(my_list[computer_chose])

        if player_chose == 0 and computer_chose == 2:
            print('You win!')
        elif player_chose == 2 and computer_chose == 0:
            print('You lose!')
        elif computer_chose > player_chose:
            print('You lose!')
        elif computer_chose < player_chose:
            print('You win!')
        elif player_chose == computer_chose:
            print('Draw!')


if __name__ == '__main__':
    rock_paper_scissors()
