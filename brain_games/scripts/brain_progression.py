import random
import sys

import prompt

sys.path.append("/home/nikon/test/project-1/python-project-49/brain_games/")
import brain_games.cli

# def initialize():
    

def get_progression():
    step = random.randint(1, 7)
    start = random.randint(0, 9)
    lenght = random.randint(5, 12)
    position = random.randint(0, lenght - 1)
    missing = start + step * position
    progression = []
    for i in range(lenght):
        progression.append(str(start + step * i))
    progression[position] = '..'
    return [progression, missing]


def init_quest(progression):
    prog = ' '.join(progression)
    print(f'Question: {prog}')


def count_answers(name):
    print('What number is missing in the progression?')
    corrects = 0
    while corrects < 3:
        data = get_progression()
        progression = data[0]
        missing = data[1]
        init_quest(progression)
        answer = prompt.string('Your answer: ')
        answer = int(answer)  
        if answer == missing:
            corrects += 1
            print('Correct!')
        else:
            corrects = 1
            print(f"'{answer}' is wrong answer ;(. Correct answer was \
            '{missing}'.")
            print(f"Let's try again, {name}!")
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')


def main():
    # initialize()
    count_answers(brain_games.cli.welcome_user())


if __name__ == "__main__":
    main()