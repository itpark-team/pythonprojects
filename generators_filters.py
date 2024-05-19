from random import randint

my_list = [randint(1, 100) for _ in range(10)]
print(my_list)

my_even_list = list(filter(lambda item: item % 2 == 0, my_list))
# for item in my_list:
#     if item % 2 == 0:
#         my_even_list.append(item)

print(my_even_list)
