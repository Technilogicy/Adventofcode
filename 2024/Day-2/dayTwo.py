import os

def checkThings(inputList: list[int]):
    errCount: int = 0
    returnVal: bool = False
    for j, t in zip(inputList, inputList[1:]):
        absol: int = abs(j-t)
        if not (absol in range(1, 4)):
            errCount += 1
    if errCount <= 1:
        returnVal = True
    else:
        print(errCount)
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

    bwaa: int = 0
    for fDIndex in fixedData:
        bwaa+= 1
        #if all(x < y for x, y in zip(fDIndex, fDIndex[1:])):
            #opType = True
        #elif all(x > y for x, y in zip(fDIndex, fDIndex[1:])):
            #opType = True
        opType = checkThings(fDIndex)
        if opType:
            count += 1
        else:
            print("Error at:", bwaa)
            
    print(count)

if __name__ == "__main__":
    main()