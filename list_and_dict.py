def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'fistname': 'Andres', 'lastname': 'Islas'}

    super_list = [
        {'fistname': 'Andres', 'lastname': 'Islas'},
        {'fistname': 'Pedro', 'lastname': 'Irnol'},
        {'fistname': 'Toño', 'lastname': 'Perez'},
        {'fistname': 'Arturo', 'lastname': 'Salmon'},
        {'fistname': 'Monse', 'lastname': 'Gala'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, '.', value)


if __name__ == '__main__':
    main()