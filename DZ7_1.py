import re
number = input("Введите автомобильный гос.номер: ")
number_reg = r"^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$"
pattern = re.compile(number_reg)
number_new = pattern.fullmatch(number)
if number_new == None:
    print('Номер не валиден!')
else:
    print(f'Номер {number} валиден, Регион {number[6:]}')
