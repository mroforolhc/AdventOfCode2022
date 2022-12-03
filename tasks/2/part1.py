import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    data = requests.get('https://adventofcode.com/2022/day/2/input', cookies={
        'session': config['session']['key']
    })

    playLetters = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    win = ['A Y', 'B Z', 'C X']
    draw = ['A X', 'B Y', 'C Z']

    count = 0

    rounds = data.text.split('\n')[0:-1]
    for round in rounds:
        count += playLetters[round[2]]

        if (round in win):
            count += 6
        elif (round in draw):
            count += 3

    return count


if __name__ == "__main__":
    print(main())
