import random

operation = 1
while operation == 1:
    ctr = 0
    t = True
    num = random.randint(1, 100)
    print('Добро пожаловать в числовую угадайку')

    def is_valid(num):
        return int(num) in range(1, 101)

    while t:
        user_num = input()
        if is_valid(user_num):
            ctr += 1
            user_num = int(user_num)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

        if user_num == num:
            print('Вы угадали, поздравляем!')
            print('Ваше количество попыток для отгадование числа:', ctr)
            print('Хотите повторить игру? Если хотите продолжить введите \'yes\'')
            operation = input()
            if operation == 'yes':
                operation = 1
            else:
                operation = 0
            t = False
        elif user_num > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок')
