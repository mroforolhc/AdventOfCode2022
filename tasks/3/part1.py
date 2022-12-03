import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def getPriority(ch):
    if ord(ch) >= 97:
        return ord(ch) - 96
    else:
        return ord(ch) - 38


def main():
    data = requests.get('https://adventofcode.com/2022/day/3/input', cookies={
        'session': config['session']['key']
    })

    packs = data.text.split('\n')[0:-1]
    sum = 0

    for pack in packs:
        letterDict = {}

        mid = len(pack) // 2
        part1 = pack[:mid]
        part2 = pack[mid:]

        for ch in part1:
            letterDict[ch] = letterDict.get(ch, 0) + 1

        for ch in part2:
            value = letterDict.get(ch)

            if value:
                sum += getPriority(ch)
                break

    return sum


if __name__ == "__main__":
    print(main())
