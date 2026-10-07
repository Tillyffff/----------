#Задание 1
# import random
# array = [random.randint(1, 150) for _ in range(1000)]
# print(array)
# def quick_sort(arr):
#   if len(arr) <= 1:
#     return arr
#   pivot = arr[len(arr) // 2]
#   left = [x for x in arr if x < pivot]  # всё, что меньше
#   middle = [x for x in arr if x == pivot]  # всё, что равно
#   right = [x for x in arr if x > pivot]  # всё, что больше
#   return quick_sort(left) + middle + quick_sort(right)
# print(quick_sort(array))

#Задание 2
# import random
# array = [random.randint(50, 100) for _ in range(100)]
# print(array)
# def quick_sort(arr):
#   if len(arr) <= 1:
#     return arr
#   pivot = arr[len(arr) // 2]
#   left = [x for x in arr if x < pivot]  # всё, что меньше
#   middle = [x for x in arr if x == pivot]  # всё, что равно
#   right = [x for x in arr if x > pivot]  # всё, что больше
#   return quick_sort(left) + middle + quick_sort(right)
# print(quick_sort(array))


#Задание 3
# import random
# def quick_sort_2d(matrix):
#   # Базовый случай если в матрице 0 или 1 строка, сортировать нечего
#   if len(matrix) <= 1:
#     return matrix
#   pivot = matrix[len(matrix) // 2][0]
#   left = [row for row in matrix if row[0] < pivot]  # Строки, где первый элемент меньше
#   middle = [row for row in matrix if row[0] == pivot]  # Строки с равным первым элементом
#   right = [row for row in matrix if row[0] > pivot]  # Строки, где первый элемент больше
#   # Рекурсивно сортируем левую и правую части и соединяем всё вместе
#   return quick_sort_2d(left) + middle + quick_sort_2d(right)
# rows, cols = 6, 3
# matrix = [[random.randint(5, 61) for _ in range(cols)] for _ in range(rows)]

# print('Исходная матрица (до сортировки):')
# for row in matrix:
#   print(row)
# sorted_matrix = quick_sort_2d(matrix)
# print('\nМатрица после сортировки первого столбца по возрастанию:')
# for row in sorted_matrix:
#   print(row)

#Задание 4
students = [
    "Кочуров Никита Владимирович",
    "Аксютичев Роман Андреевич",
    "Сахаров Максим Дмитриевич",
    "Байрамалов Евгений Сергеевич",
    "Степаненко Елизавета Андреевна",
    "Артемчук Виктор Александрович",
    "Соболев Илья Николаевич",
    "Белов Илья Петрович",
    "Шаронова Вероника Александровна",
    "Александров Алексей Евгеньевич",
    "Сумароков Кирилл Олегович",
    "Бурмистров Владимир Дмитриевич",
    "Рамазанов Рамазан Мухтарович",
    "Асютин Иван Дмитриевич",
    "Попкова Дарья Андреевна",
    "Ветров Михаил Евгеньевич",
    "Попович Ана-Анастасия",
    "Владимиров Вадим Игоревич",
    "Никулин Дмитрий Михайлович",
    "Галимов Ильяс Ирекович",
    "Мордовочкина Варвара Александровна",
    "Демьянов Павел Евгеньевич",
    "Минаев Никита Дмитриевич",
    "Еланцев Андрей Павлович",
    "Матюхин Дмитрий Михайлович",
    "Звонарев Николай Константинович",
    "Маслобойщиков Тимур Андреевич",
    "Казаринов Андрей Владимирович",
    "Кирьяков Илья Владимирович",
    "Савин Иван Артемович",
    "Салдин Максим Витальевич",
]
print("--- Список до сортировки ---")
for s in students:
  print(s)

students.sort()
print("\n--- Список после сортировки по алфавиту ---")
for s in students:
  print(s)