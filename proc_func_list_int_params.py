# def double_number(number):
#     number = number * 2
#     print("double_number: ", number)


# number = 10
# print(number)
# double_number(number)
# print(number)


def double_heights(heights):
    for index in range(len(heights)):
        heights[index] = heights[index] * 2


heights = [160, 200, 170]

print(heights)
double_heights(heights)
print(heights)
