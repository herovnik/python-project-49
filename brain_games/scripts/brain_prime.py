import random
import sys

import prompt

sys.path.append("/home/nikon/test/project-1/python-project-49/brain_games/")
import math

import brain_games.cli


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

# def initialize():
    

def get_count():
    return random.randint(0, 100)


def init_quest(count):
    print(f'Question: {count}')


def count_answers(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    corrects = 0
    while corrects < 3:
        count = get_count()
        init_quest(count)
        answer = prompt.string('Your answer: ')  
        if answer.lower() == 'no' and is_prime(count) is False:
            corrects += 1
            print('Correct!')
        elif answer.lower() == 'yes' and is_prime(count) is True:
            corrects += 1
            print('Correct!')
        elif answer.lower() != 'yes' and is_prime(count) is True:
            corrects = 1
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif answer.lower() != 'no' and is_prime(count) is False:
            corrects = 1
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')


def main():
    # initialize()
    count_answers(brain_games.cli.welcome_user())


if __name__ == "__main__":
    main()

