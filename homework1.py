# Строки и индексация строк
example = 'Программирование+'# 1. присваиваем значение переменной example (нечетное число символов)
print(example[0])# 2. выводим первый символ строки
print(example[-1])# 3. выводим последний символ строки
length = len(example)# вычисляем длину строки
number3 = length // 2# находим индекс второй половины строки с нечётным количеством символов
print(example[number3:])# 4. выводим вторую половину строки с нечётным количеством символов
print(example[::-1])# 5. выводим символы строки в обратном порядке
print(example[1::2])# 6. выводим каждый второй символ строки
