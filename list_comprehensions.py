def main():
    # square = []
    # for element in range(1,101):
    #     element = element**2
    #     if element % 3 != 0:
    #         square.append(element)

    square = [element**2 for element in range(1, 101) if element % 3 != 0]

    #only multiple of 4 which is also multiplo of 6 and 9.
    square_two = [[element for element in range(1, 100_000) if element % 36 == 0]]

    print(square_two)

if __name__ == '__main__':
    main()