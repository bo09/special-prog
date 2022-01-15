while True:

    x = input('\nВыберите операцию | + | - | * | / |: ')

    if x == '+' or x == '-' or x == '/' or x == '*':
        y = int(input('\nСколько операндов? '))

        if x == '+':
            summ = 0
            line = ''
            for i in range(1, y + 1):
                num = int(input(f'Введите операнд {i}: '))
                if i == 1:
                    summ += num
                    line += str(num)
                else:
                    summ += num
                    line += f' + {str(num)}'
            print(f'\n{line} = {summ}')
            break

        elif x == '-':
            summ = 0
            line = ''
            for i in range(1, y + 1):
                num = int(input(f'Введите операнд {i}: '))
                if i == 1:
                    summ += num
                    line += str(num)
                else:
                    summ -= num
                    line += f' - {str(num)}'
            print(f'\n{line} = {summ}')
            break

        elif x == '*':
            summ = 0
            line = ''
            for i in range(1, y + 1):
                num = int(input(f'Введите операнд {i}: '))
                if i == 1:
                    summ += num
                    line += str(num)
                else:
                    summ *= num
                    line += f' * {str(num)}'
            print(f'\n{line} = {summ}')
            break

        elif x == '/':
            summ = 0
            line = ''
            for i in range(1, y + 1):
                num = int(input(f'Введите операнд {i}: '))
                if i == 1:
                    summ += num
                    line += str(num)
                else:
                    summ /= num
                    line += f' / {str(num)}'
            print(f'\n{line} = {summ}')
            break

    else:
        print('\nОшибка: такой операции не существует. Попробуйте ещё раз.')