# Неизменяемые и изменяемые объекты. Кортежи и списки
# Цель:
# Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами.
immutable_var = ('Project',5,2.9,True,'L')
print(immutable_var)
print(type(immutable_var))
# Тип 'tuple' - неизменяемый, поэтому при попытке изменить значение, выдается ошибка
mutable_list = ['Project',5,2.9,True,'L']# Присваиваем те же значения, что и immutable_var
print(mutable_list)# Видим, что значения такие же
print(type(mutable_list))# Тип 'list', значит изменения возможны
mutable_list[0] = False# Меняем значение первого элемента
mutable_list[4] = 'list'# Меняем значение пятого элемента
mutable_list.remove(2.9)# Удаляем элемент со значением 2.9
mutable_list.append('Test')# Добавляем элемент Test
print(mutable_list)# Убеждаемся, что все изменения прошли