def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as num:
        for line in num:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Andres", "Armando", "Gerardo", "Paola"]
    with open("./files/numbers.txt", "a", encoding="utf-8") as num:
        for name in names:
            num.write(name)
            num.write("\n")
    print(names)


def main():
    #read()
    write()


if __name__ == '__main__':
    main()