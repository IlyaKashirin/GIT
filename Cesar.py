alfavit_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = int(input('Шаг шифровки: '))
message = input("Сообщение для шифровки: ").upper()
encrypt = ''
for i in message:
        index = alfavit_ru.find(i)
        new_index = index + key
        encrypt += alfavit_ru[new_index]
print (f'Зашифрованное сообщение: {encrypt}')

vybor = input('Выполнить расшифровку, Да/Нет: ')

if vybor == 'Да':
    decrypt = ''
for i in encrypt:
    index_dec = alfavit_ru.find(i)
    new_index_dec = index_dec - key
    decrypt += alfavit_ru[new_index_dec]
else:
    pass
print(f'Расшифрованное сообщение: {decrypt}')



