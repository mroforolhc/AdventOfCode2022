import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    data = requests.get('https://adventofcode.com/2022/day/4/input', cookies={
        'session': config['session']['key']
    })

    sum = 0

    groups = list(map(
        lambda group: list(map(
            lambda part: list(map(int, part.split('-'))),
            group.split(',')
        )),
        data.text.split('\n')[:-1]
    ))

    for group in groups:
        if (group[0][0] >= group[1][0] and group[0][1] <= group[1][1]) \
            or (group[0][0] <= group[1][0] and group[0][1] >= group[1][1]):
            sum += 1

    return sum


if __name__ == "__main__":
    print(main())
