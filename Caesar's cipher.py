lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

move = input('Выбери действие: ш - шифрование, д - дешифрование: ')
while move != 'ш' and move != 'д':
    move = input('Ты что-то не так ввел. Выбери действие: ш - шифрование, д - дешифрование: ')

language = input('Выбери язык: р - русский, а - английский: ')
while language != 'а' and language != 'р':
    language = input('Ты что-то не так ввел. Выбери язык: р - русский, а - английский: ')

step = int(input('Введи шаг: '))
text = input('Введите текст: ')
symbols_to_ignore = ' ,.!?_-'
result = ''

if move == 'д':
    step = -step

if language == 'р':
    for letter in text:
        if letter in lower_rus_alphabet and letter not in symbols_to_ignore and letter.islower():
            result += lower_rus_alphabet[(lower_rus_alphabet.find(letter) + step) % len(lower_rus_alphabet)]

        elif letter.lower() in lower_rus_alphabet and letter not in symbols_to_ignore and letter.isupper():
            result += lower_rus_alphabet[(lower_rus_alphabet.find(letter.lower()) + step) % len(lower_rus_alphabet)].upper()

        elif letter in symbols_to_ignore:
            result += letter


elif language == 'а':
    for letter in text:
        if letter in lower_eng_alphabet and letter not in symbols_to_ignore and letter.islower():
            result += lower_eng_alphabet[(lower_eng_alphabet.find(letter) + step) % len(lower_eng_alphabet)]

        elif letter.lower() in lower_eng_alphabet and letter not in symbols_to_ignore and letter.isupper():
            result += lower_eng_alphabet[(lower_eng_alphabet.find(letter.lower()) + step) % len(lower_eng_alphabet)].upper()

        elif letter in symbols_to_ignore:
            result += letter
        
print('\n', result)