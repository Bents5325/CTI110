# Math Quiz
# 11/21/2022
# CTI-110 P5HW2 - Math Quiz
# Shauntae Bent
#

import random
def print_menu():
    print('MAIN MENU')
    print('-----------------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()
    menu_op = input('Please choose one of the menu options: ')
    
    if menu_op == '1':
        add_random_nums()
    elif menu_op == '2':
        subtract_random_nums()
    elif menu_op == '3':
        print('Thank you for playing!')
        print('Bye!!')
    else:
        print()
        print('!!!INVALID OPTION!!!')
        print()
        print_menu()
        

def add_random_nums():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    print(f'   {num1}')
    print(f'+  {num2}')
    answer = num1 + num2
    num_of_guesses = 1
    user_guess = int(input('Enter Answer: '))

    while user_guess != answer:
        if user_guess > answer:
            print('Sorry, guess was too high')
            print()
            user_guess = int(input('Try again: '))
            num_of_guesses += 1
        elif user_guess < answer:
            print('Sorry, guess was too  low')
            print()
            user_guess = int(input('Try again: '))
            num_of_guesses += 1
    print('You answered correctly!')
    print(f'Number of guesses: {num_of_guesses}')
    print()
    print_menu()

def subtract_random_nums():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    print(f'   {num1}')
    print(f'-  {num2}')
    answer = num1 - num2
    num_of_guesses = 1
    user_guess = int(input('Enter Answer: '))

    while user_guess != answer:
        if user_guess > answer:
            print('Sorry, guess was too high')
            print()
            user_guess = int(input('Try again: '))
            num_of_guesses += 1
        elif user_guess < answer:
            print('Sorry, guess was too  low')
            print()
            user_guess = int(input('Try again: '))
            num_of_guesses += 1
    print('You answered correctly!')
    print(f'Number of guesses: {num_of_guesses}')
    print()
    print_menu()

print('Welcome to Math Quiz')
print()
print_menu()
