question = "вопро вопрос вопрос"
right_answer = "собака"
my_answer = ["*"] * len(right_answer)

game_over = False

while game_over == False:

    my_answer_as_string = "".join(my_answer)
    print(f"моё слово сейчас {my_answer_as_string}")

    print("введите предполагаемую букву:", end=" ")
    letter = input()

    if right_answer.find(letter) != -1:
        for index, _ in enumerate(right_answer):
            if right_answer[index] == letter:
                my_answer[index] = letter

    has_star = "*" in my_answer
    if has_star == False:
        game_over = True

print("Поздравляю игра окончена вы победили")

my_answer_as_string = "".join(my_answer)
print(f"Итоговое слово {my_answer_as_string}")
