import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    data = requests.get('https://adventofcode.com/2022/day/6/input', cookies={
        'session': config['session']['key']
    })

    arData = list(data.text.strip())

    for i in range(14, len(arData)):
        words = arData[i - 14:i]
        setWords = set(words)

        if (len(words) == len(setWords)):
            return i

    len(arData)

if __name__ == "__main__":
    print(main())
