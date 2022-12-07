import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    data = requests.get('https://adventofcode.com/2022/day/7/input', cookies={
        'session': config['session']['key']
    })

    lines = data.text.split('\n')[1:-1]

    fs = {
        '/': {}
    }

    parentFs = None
    currentFs = fs['/']

    for line in lines:
        lineParts = line.split(' ')

        if (lineParts[0] == '$'):
            if (lineParts[1] == 'cd'):
                if (lineParts[2] == '..'):
                    currentFs = parentFs
                else:
                    parentFs = currentFs
                    currentFs[lineParts[2]] = {}
                    currentFs = currentFs[lineParts[2]]
        elif (lineParts[0] != 'dir'):
            currentFs[lineParts[1]] = lineParts[0]


if __name__ == "__main__":
    print(main())
