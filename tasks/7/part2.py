import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    data = requests.get('https://adventofcode.com/2022/day/7/input', cookies={
        'session': config['session']['key']
    })

    lines = data.text.split('\n')[1:-1]

    mem = {}
    currentPath = ['']

    for line in lines:
        lineParts = line.split(' ')

        if (lineParts[0] == '$'):
            if (lineParts[1] == 'cd'):
                if (lineParts[2] == '..'):
                    currentPath.pop()
                else:
                    currentPath.append(lineParts[2])
        elif (lineParts[0] != 'dir'):
            for i in range(len(currentPath)):
                path = '/'.join(currentPath[:i + 1])
                mem[path] = mem.get(path, 0) + int(lineParts[0])

    sortMem = list(mem.values())
    sortMem.sort()

    needDel = 30000000 - (70000000 - mem[''])

    for value in sortMem:
        if (needDel <= value):
            return value


if __name__ == "__main__":
    print(main())
