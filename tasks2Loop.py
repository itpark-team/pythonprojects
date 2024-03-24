start_number = int(input("введите стартовое число: "))
finish_number = int(input("введите конечное число: "))
step = int(input("введите шаг приращения: "))

# i = start_number

# while i <= finish_number:
#     print(i, end=" ")
#     i = i + step

i = finish_number

while i >= start_number:
    print(i, end=" ")
    i = i - step