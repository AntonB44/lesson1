# Практическое задание по теме: "Словари и множества"
# Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.
# Работа со словарями:
my_dict = {'Anton': 1964,'Igor':1975,'Nikolay':1947,'Dima':2009}
print(my_dict)
print(my_dict['Nikolay'])# вывод на экран существующего значения
print(my_dict.get('Ilya'))# вывод на экран несуществующего значения
my_dict['Tanya'] = 1977# добавляем в словарь жлемент
my_dict['Vova'] = 1985# добавляем в словарь еще один элемент
del_1 = my_dict.pop('Dima')# запоминаем значение элемента, которое удаляем из словаря
print(del_1)# вывод на экран значения удаленного элемента
print(my_dict)# вывод на экран измененного словаря
# Работа с множествами:
my_set = {1,3,5,4,5,4,'find','go','go',5.3,5.3}
print(my_set)# Проверяем, что выводятся только уникальные значения
my_set.add('Gosha')# Добавляем новый элемент
my_set.add(789)# Добавляем еще один новый элемент
my_set.discard('go')# Удаляем существующий элемент
print(my_set)# Проверяем внесенные изменения в множество
