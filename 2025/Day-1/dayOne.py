import os

def main():
    # things
    data: list[str] = []
    fixedData: list[str] = []
    i: int = 0
    status: int = 50
    count: int = 0
    countOther: int = 0
    j: str
    l: int = 0
    # file
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        data = file.readlines()
    # fix it
    for i in range(len(data)):
        fixedData.append(data[i].strip())
    # main loop of stuff
    for j in data:
        # get the number of times
        i = int(j[1:])
        # just a quick check for if it's 0
        if status == 0:
            count += 1
        # check what way it goes
        if j[0] == "L":
            # loop subtract
            for l in range(i):
                status -= 1
                # underflow and track
                if status < 0:
                    countOther += 1
                    status = 99
        else:
            # loop add
            for l in range(i):
                status += 1
                # overflow and track
                if status > 99:
                    countOther += 1
                    status = 0
    # print all the stuff
    print(l, count, countOther)
    print(count + countOther)

if __name__ == "__main__": 
    main()