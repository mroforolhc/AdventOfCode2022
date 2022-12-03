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
    groups = [packs[i:i+3] for i in range(0, len(packs), 3)]
    sum = 0

    for group in groups:
        letterDict = {}

        for pack in group:
            letterPack = {}

            for ch in pack:
                if (not letterPack.get(ch)):
                    letterPack[ch] = 1
                    letterDict[ch] = letterDict.get(ch, 0) + 1

        ch = list(letterDict.keys())[list(letterDict.values()).index(3)]
        sum += getPriority(ch)

    return sum


if __name__ == "__main__":
    print(main())
