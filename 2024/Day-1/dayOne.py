import os

def main():
    lines: list[str] = []
    lineOne: list[int] = []
    lineTwo: list[int] = []
    line: str
    num1: int = 0
    num2: int = 0
    total: int = 0
    simScore: int = 0
    i: int = 0
    tNum: int = 0
    sNum: int = 0
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        num1, num2 = map(int, line.split())
        lineOne.append(num1)
        lineTwo.append(num2)
    lineOne.sort()
    lineTwo.sort()
    for i in range(len(lines)):
        total += abs(lineOne[i] - lineTwo[i])
    print(total)

    for tNum in lineOne:
        count: int = 0
        for sNum in lineTwo:
            if sNum == tNum:
                count += 1
        simScore += (tNum * count)
    print(simScore)

if __name__ == "__main__":
    main()