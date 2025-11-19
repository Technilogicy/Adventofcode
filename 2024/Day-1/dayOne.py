def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    for line in lines:
        line.strip
        print(line)

if __name__ == "__main__":
    main()