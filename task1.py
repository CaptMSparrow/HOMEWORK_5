class InconsistentDataError(Exception):
    pass


class NonNumericError(Exception):
    pass


print('Var1')
line1 = input('Введите первые катеты: ')
line2 = input('Введите вторые катеты: ')
line1_new = line1.replace(' ', '')
line2_new = line2.replace(' ', '')


# line1 = [float(num) for num in line1.split()]


if (line1_new.isdigit() and line2_new.isdigit()) is not True:
    raise NonNumericError('Введены были не числа')

a = line1.split(' ')
b = line2.split(' ')

if len(a) != len(b):
    raise InconsistentDataError('Нечетное количество катетов')

for index1, (leg1_1, leg2_1) in enumerate(zip(a, b), 1):
    leg1_1, leg2_1 = float(leg1_1), float(leg2_1)
    c1 = (leg1_1**2 + leg2_1**2) ** 0.5
    S1 = leg1_1*leg2_1 / 2
    print(f'Треугольник {index1} с катетами {leg1_1} и {leg2_1}', end=' ')
    print(f'имеет площадь {S1} и гипотенузу {c1}')

print('Var2')
line = input('Введите катеты: ')
line_new = line.replace(' ', '')

if line_new.isdigit() is not True:
    raise NonNumericError('Введены были не числа')

a_and_b = line.split(' ')

if len(a_and_b) % 2 != 0:
    raise InconsistentDataError('Нечетное количество катетов')

leg1, leg2 = [], []
for index in range(len(a_and_b)):
    if index % 2 == 0:
        leg1.append(a_and_b[index])
    else:
        leg2.append(a_and_b[index])
for index2, (leg1_2, leg2_2) in enumerate(zip(leg1, leg2), 1):
    leg1_2, leg2_2 = float(leg1_2), float(leg2_2)
    c2 = (leg1_2**2 + leg2_2**2) ** 0.5
    S2 = leg1_2*leg2_2 / 2
    print(f'Треугольник {index2} с катетами {leg1_2} и {leg2_2}', end=' ')
    print(f'имеет площадь {S2} и гипотенузу {c2}')
