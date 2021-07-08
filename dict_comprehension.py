def main():
    # my_dict = {}

    # for element in range(1,101):
    #     if element % 3 != 0:
    #         my_dict[element] = element**3

    my_dict = {element: element**3 for element in range(1, 101) if element % 3 != 0}

    my_dict_two = {element: element**0.5 for element in range(1,1001)}

    print(my_dict_two)


if __name__ == '__main__':
    main()