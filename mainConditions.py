print("введите символ: ", end="")
symbol = input()

if symbol >= "a" and symbol <= "z" or symbol >= "A" and symbol <= "Z":
    print("это буква")
elif symbol >= "0" and symbol <= "9":
    print("это цифра")
else:
    print("неизвестный науке символ")