import os

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        lines = file.readlines()
    
    lineOne: list[int] = []
    lineTwo: list[int] = []
    num1: int
    num2: int
    total: int = 0
    simScore: int = 0
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