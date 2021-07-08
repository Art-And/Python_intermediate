def divisor(num):
    divisor = [element for element in range(1, num + 1) if num % element == 0]

    return divisor

def main():
    try:
        num = int(input('Pleas set a number: '))
        if num < 0:
            raise ValueError('Set a positive number')
        print(divisor(num))

        print('The program finish')
    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    main()