
stroka = input('Введите строку: ')
offset = int(input('Введите количество символов для среза: '))
repetitions = int(input('Введите количество повторений строки: '))
def trim_and_repeat(stroka,offset,repetitions):
    for i in range(repetitions):
        print(stroka[offset:],end = '')

trim_and_repeat(stroka,offset,repetitions)


