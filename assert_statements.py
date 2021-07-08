def divisor(num):
    divisor = [element for element in range(1, num + 1) if num % element == 0]

    return divisor

def main():
    num = input('Pleas set a number: ')
    #isnumeric() only works if it's a string
    assert num.isnumeric() and int(num) > 0, 'Please set a positive number'

    print(divisor(int(num)))

    print('The program finish')


if __name__ == '__main__':
    main()