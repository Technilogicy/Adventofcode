import os

def checkThings(inputList: list[int]):
    returnVal: bool = False
    if all(x < y for x, y in zip(inputList, inputList[1:])):
        returnVal = True
    elif all(x > y for x, y in zip(inputList, inputList[1:])):
        returnVal = True
    for j, t in zip(inputList, inputList[1:]):
        absol: int = abs(j-t)
        if not (absol in range(1, 4)):
            returnVal = False
    return returnVal

def brute(input: list[int]):
    tNewList: list[int] = []
    i: int = 0
    returnVal: bool = False
    for i in range(len(input)):
        tNewList = []
        j: int = 0
        for j in input:
            tNewList.append(j)
        tNewList.pop(i)
        if checkThings(tNewList):
            print(input, tNewList)
            returnVal = True
    return returnVal

def main():
    # declare the vars and types
    data: list[str] = []
    fixedData: list[list[int]] = []
    fDIndex: list[int] = []
    i: int = 0
    count: int = 0
    opType: bool = False
    # Get the data
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        data = file.readlines()
    
    # Fix the data
    for i in range(len(data)):
        fullLine: list[int]
        fullLine = list(map(int, data[i].strip().split(" ")))
        fixedData.append(fullLine)

    for fDIndex in fixedData:
        opType = checkThings(fDIndex)
        if not opType:
            opType = brute(fDIndex)
        if opType:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()