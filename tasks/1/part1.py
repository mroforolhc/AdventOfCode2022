import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    data = requests.get('https://adventofcode.com/2022/day/1/input', cookies={
        'session': config['session']['key']
    })

    elves = data.text.split('\n\n')
    sumCalories = []

    for elf in elves:
        foods = elf.split('\n')
        sumFoods = 0

        for food in foods:
            if (food):
                sumFoods += int(food)

        sumCalories.append(sumFoods)

    sumCalories.sort()
    return sumCalories[-1]


if __name__ == "__main__":
    print(main())
