"""Пишем игру. Программа выбирает из диапазона чисел (пусть для начала будет 1-100) случайное число и предлагает пользователю его угадать. Пользователь вводит число. Если пользователь не угадал - предлагает пользователю угадать еще раз, пока он не угадает. Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить. N - Прекратить."""
import random


def new_game():
    val = input("Do you want start New Game?")
    start_new_game = choose(val)

    if start_new_game is True:
        return main(1, 100, 3)

    return 'The End'


def clue(guess_number, hidden_number):
    result = guess_number - hidden_number
    if abs(result) > 10:
        return print('cold')
    if 10 >= abs(result) >= 5:
        return print('heat')
    if 5 > abs(result) >= 1:
        return print('hot')


def choose(val=False):
    boolian = False

    while True:
        if val == 'y':
            boolian = True
            break
        elif val == 'n':
            boolian = False
            break
        else:
            val = input("Value error! Try again! Just('y' or 'n')")
            continue

    return boolian


def main(rand_start, rand_stop, attempts):
    attempts_counter = attempts
    hidden_number = random.randint(rand_start, rand_stop)

    while attempts_counter > 0:
        guess_number = input(f'Enter an integer from {rand_start} to {rand_stop}: ')
        if guess_number.isdigit():
            guess_number = int(guess_number)
            if guess_number == hidden_number:
                attempts_counter = 0
            else:
                clue(guess_number, hidden_number)
                attempts_counter -= 1
                if attempts_counter == 0:
                    print("You didn't guess. You don't have attempts left")
                else:
                    print(f"You didn't guess. You have {attempts_counter} attempts left")
                    val = input('Want to try again?')
                if choose(val) is False:
                    attempts_counter = 0
        else:
            print('Enter whole numbers only.')
            continue

    return new_game()


if __name__ == '__main__':
    print(main(1, 100, 3))
