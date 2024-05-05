alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
key = 12
originalString = "мама мыла, раму с мыслом!!!"
encodeString = ""

for letter in originalString:
    letter_index_in_alphabet = alphabet.find(letter)

    if letter_index_in_alphabet != -1:
        new_letter_index_in_alphabet = (letter_index_in_alphabet + key) % len(alphabet)
        encodeString = encodeString + alphabet[new_letter_index_in_alphabet]
    else:
        encodeString = encodeString + letter

print(encodeString)
