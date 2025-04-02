import random
import sys

import prompt

sys.path.append("/home/nikon/test/project-1/python-project-49/brain_games/")
import brain_games.cli

# def initialize():
    

def get_expression():
    a = random.randint(0, 50)
    b = random.randint(0, 50)
    oper = random.randint(0, 2)
    opers = ['+', '-', '*']
    return f'{str(a)} {opers[oper]} {str(b)}'


def init_quest(expression):
    print(f'Question: {expression}')


def count_answers(name):
    print('What is the result of the expression?')
    corrects = 0
    while corrects < 3:
        expression = get_expression()
        init_quest(expression)
        answer = prompt.string('Your answer: ')
        right_answer = int(eval(expression))  
        if int(answer) == right_answer:
            corrects += 1
            print('Correct!')
        else:
            corrects = 1
            print(f"'{answer}' is wrong answer ;(. Correct answer was \
             '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')


def main():
    # initialize()
    count_answers(brain_games.cli.welcome_user())


if __name__ == "__main__":
    main()