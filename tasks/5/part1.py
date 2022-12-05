import configparser
import requests

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    data = requests.get('https://adventofcode.com/2022/day/5/input', cookies={
        'session': config['session']['key']
    })

    data = data.text.split('\n\n')
    dataBoxes = data[0].split('\n')
    dataMoves = data[1][:-1].split('\n')

    boxes = [[] for i in range(9)]

    for string in dataBoxes:
        for i, char in enumerate(string):
            if (ord(char) >= 65 and ord(char) <= 90):
                index = i // 4
                boxes[index].insert(0, char)

    for move in dataMoves:
        temp = move.replace('move ', '').replace(' from ', ',').replace(' to ', ',')
        nums = list(map(int, temp.split(',')))

        indexFrom = nums[1] - 1
        indexTo = nums[2] - 1

        # можно и лучше
        for i in range(nums[0]):
            box = boxes[indexFrom].pop()
            boxes[indexTo].append(box)

    result = []
    for string in boxes:
        result.append(string[-1])

    return ''.join(result)


if __name__ == "__main__":
    print(main())
