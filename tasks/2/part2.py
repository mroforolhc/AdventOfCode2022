import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    data = requests.get('https://adventofcode.com/2022/day/2/input', cookies={
        'session': config['session']['key']
    })

    result = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    rock = ['A Y', 'B X', 'C Z']
    paper = ['A Z', 'B Y', 'C X']
    scissors = ['A X', 'B Z', 'C Y']

    count = 0

    rounds = data.text.split('\n')[0:-1]
    for round in rounds:
        count += result[round[2]]

        if (round in rock):
            count += 1
        elif (round in paper):
            count += 2
        elif (round in scissors):
            count += 3

    return count


if __name__ == "__main__":
    print(main())
