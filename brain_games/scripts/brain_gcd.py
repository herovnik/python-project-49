import random
import prompt
import math
import sys
sys.path.append("/home/nikon/test/project-1/python-project-49/brain_games/")
import brain_games.cli

#def initialize():
    

def get_count():
    return [random.randint(0, 100), random.randint(0, 100)]

def init_quest(count):
    print(f'Question: {count[0]} {count[1]}')

def count_answers(name):
    print('Find the greatest common divisor of given numbers.')
    corrects = 0
    while corrects < 3:
        count = get_count()
        init_quest(count)
        answer = int(prompt.string('Your answer: ')) 
        correct_answer = math.gcd(count[0], count[1])
        if answer == correct_answer:
            corrects += 1
            print('Correct!')
        else:
            corrects = 1
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if corrects == 3:
        print(f'Congratulations, {name}!')

def main():
    #initialize()
    count_answers(brain_games.cli.welcome_user())

if __name__ == "__main__":
    main()