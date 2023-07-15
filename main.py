"""
RPS GAME DESCRIPTION: {MADE BY MISALLAM}

A classic two-person game where players start each round by saying, “rock, paper, scissors, shoot!”
On “shoot,” each player holds out their fist for rock, flat hand for paper, or their index and middle finger for scissors.

1. Rock crushes scissors
2. Scissors cut paper.
3. Paper covers rock.
"""

import random
import time
from tqdm import tqdm

# Game counters and conditions

total_plays = 0
user_winnings = 0
total_play_time = 0
flag = True

name = input('\nType your name buddy: \n').strip()
print()

# For limiting the attempts of choosing gender

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    gender = input('Choose your gender (M/F): ')
    if gender.lower() == 'm':
        fname = 'Mr. ' + name.capitalize().split(" ")[0]
        break
    elif gender.lower() == 'f':
        fname = 'Ms. ' + name.capitalize().split(" ")[0]
        break
    else:
        print('Please enter "M" or "F"')
        attempts += 1
print()

if attempts == max_attempts:
    print('Too many invalid attempts. Exiting the program.')
    exit()

# Make a while loop with a True flag to help restart the game with thw same info {from above} every time user choose to play again

while flag == True:
    total_plays += 1

    print(f'Let\'s Start our rock, paper, scissors interactive game, {fname}:')
    print()

    options = ['Rock', 'Paper', 'Scissors']

    print('Please choose one of the following: ')
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")
    print()

    start_point = time.time()

    while True:
        try:
            user_play = int(
                input('Please choose one number corresponding to your choice from the list: '))
            if user_play in range(1, len(options) + 1):
                print(f"You have selected: {options[user_play - 1]}")
                break
            else:
                print(
                    f'Please input a valid choice from (1 to {len(options)}), {fname}!')
        except ValueError:
            print(
                f'Please input a valid choice from (1 to {len(options)}), {fname}!')
    end_point = time.time()
    user_play_time = int(end_point - start_point)

    print(f'\nYou took {user_play_time} seconds to make your move.')
    print()

    pc_play = 0

    while True:
        pc_play = random.randint(1, len(options))
        if pc_play != user_play:
            break

    print('Now it\'s the A.I. system turn!')

    print(
        """
    ████████╗██╗░░██╗██╗███╗░░██╗██╗░░██╗██╗███╗░░██╗░██████╗░
    ╚══██╔══╝██║░░██║██║████╗░██║██║░██╔╝██║████╗░██║██╔════╝░
    ░░░██║░░░███████║██║██╔██╗██║█████═╝░██║██╔██╗██║██║░░██╗░
    ░░░██║░░░██╔══██║██║██║╚████║██╔═██╗░██║██║╚████║██║░░╚██╗
    ░░░██║░░░██║░░██║██║██║░╚███║██║░╚██╗██║██║░╚███║╚██████╔╝
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░ ██░██░██░██░██░
    """, end="")

    print()
    for i in tqdm(range(5), desc="Processing", ascii=True):
        time.sleep(2)
        print("", end="", flush=True)

    print()
    print(f'The A.I. system have selected: {options[pc_play - 1]} \n')

    if user_play == pc_play:
        print('That\'s a tie buddy!')  # Just to make sure!
    elif (user_play == 1 and pc_play == 3) or (user_play == 2 and pc_play == 1) or (user_play == 3 and pc_play == 2):
        user_winnings += 1
        print("""

    ██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗  ██╗██╗██╗
    ╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║  ██║██║██║
    ░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║  ██║██║██║
    ░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║  ╚═╝╚═╝╚═╝
    ░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║  ██╗██╗██╗
    ░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝╚═╝╚═╝
    """)
    else:
        print("""
         
    ░█████╗░██╗      ░██╗░░░░░░░██╗██╗███╗░░██╗░██████╗
    ██╔══██╗██║      ░██║░░██╗░░██║██║████╗░██║██╔════╝
    ███████║██║      ░╚██╗████╗██╔╝██║██╔██╗██║╚█████╗░
    ██╔══██║██║      ░░████╔═████║░██║██║╚████║░╚═══██╗
    ██║░░██║██║      ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝
    ╚═╝░░╚═╝╚═╝ ██    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░
    """)

    total_play_time += user_play_time

    print()

    while True:
        trial = input('Do you wanna play again? Please enter only Y/N: ')
        if trial.lower() == 'y':
            flag = True
            break
        elif trial.lower() == 'n':
            flag = False
            break
        else:
            print(f'Please enter only y or n {fname}: ')
            continue

if flag == False:
    print('\nIt was a pleasure having you as our player, let\'s see some statistics about you before you leave:\n')
    print(
        f'* Your total playes are {total_plays} times.\n* You won {user_winnings} of them.\n* On the other hand, you lost {total_plays - user_winnings} of them.\n* You spent {int(total_play_time)} second making your best moves.')

    print(f'\nThank you for stepping by {fname}\n')
