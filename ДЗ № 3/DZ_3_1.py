
fro = int(input('Введи первое число: '))
to = int(input('Введи второе число: '))
def sum_distance(fro,to):
    sum = 0
    if fro < to:
        for i in range(fro,to+1):
            sum += i
        print(sum)
    else:
        for i in range(to,fro+1):
            sum += i
        print(sum)
sum_distance(fro,to)
print('Коммит')#


