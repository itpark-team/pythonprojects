import os

clear_screen = lambda: os.system("clear")  # for linux and macos
# clear = lambda: os.system("cls")  # for windows

guessed_word = input("Введите слово: ")
hint = input("Введите подсказку: ")

answer_word = ["*"] * len(guessed_word)


game_over = False


while game_over == False:
    clear()

    answer_word_as_string = "".join(answer_word)
    print(f"Вы отгадали: {answer_word_as_string}")

    print(f"Подсказка: {hint}")
    answer_letter = input("Введите предполагаемую букву загаданного слова: ")

    has_answer_letter = answer_letter in guessed_word

    if has_answer_letter == True:
        print("Отлично, такая буква есть. Нажмите <Enter>")
        for index, _ in enumerate(guessed_word):
            if answer_letter == guessed_word[index]:
                answer_word[index] = answer_letter
    else:
        print("Такой буквы нет. Нажмите <Enter>")

    input()  # wait enter

    has_star = "*" in answer_word

    if has_star == False:
        game_over = True

print("Поздравляем вы победили")

answer_word_as_string = "".join(answer_word)
print(f"Загаданное слово было: {answer_word_as_string}")
