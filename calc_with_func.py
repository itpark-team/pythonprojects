def input_int_number(message):
    is_correct_input = False

    while is_correct_input == False:
        try:
            number = int(input(message))
            is_correct_input = True
        except:
            print("ошибка. ввели НЕ ЦЕЛОЕ число. повторите ввод.")

    return number


def get_sum(number1, number2):
    return number1 + number2


def print_sum(number1, number2, sum):
    print(f"{number1} + {number2} = {sum}")


def main():
    number1 = input_int_number("введите целое число 1: ")
    number2 = input_int_number("введите целое число 2: ")

    sum = get_sum(number1, number2)

    print_sum(number1, number2, sum)


main()
