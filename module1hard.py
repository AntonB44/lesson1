# Задание "Средний балл":
'''Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}'''
'''Напишите программу, которая составляет словарь, используя grades и students, 
где ключом будет имя ученика, а значением - его средний балл.'''
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Решаем без использования опреторов циклов
grades_average = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),
                sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),
                sum(grades[4])/len(grades[4])]# создаем список со средними оценками в том же порядке
print(grades_average)# проверяем правильность вычисления средних оценок
students_sorted = sorted(students)# сортируем множество студентов (по условию задачи)
print(students_sorted)# проверяем сортировку
students_dict = dict(zip(students_sorted,grades_average))# создаем искомый словарь
print(students_dict)# выводим на экран решение