
# Задание №1 (easy)

# вариант с постоянной (10) длиной строки на выходе

# a = ["Яблоко", "Лимон", "Апельсин", "Груша"]
# for i in range(len(a)):
#     print(str(i+1)+'.', a[i].rjust(10))

# вариант с универсальной для любого списка длиной строки на выходе

# a = ['Яблоко', 'Груша', 'Апельсин', 'Банан', 'Грейпфрут']
# max_a = len(a[0])
# for i in a:
#     if len(i) >= max_a:
#         max_a = len(i)
# for i in range(len(a)):
#     print(str(i+1)+'.', a[i].rjust(max_a))

# варианты с использованием метода .format

# a = ['Яблоко', 'Груша', 'Апельсин', 'Банан', 'Грейпфрут']
# for i in range(len(a)):
#     print('{}.{:>10}'.format(i+1, a[i]))


# a = ['Яблоко', 'Груша', 'Апельсин', 'Банан', 'Грейпфрут']
# max_a = len(a[0])
# for i in a:
#     if len(i) >= max_a:
#         max_a = len(i)
# for i in range(len(a)):
#     print('{}.{:>max_a}'.format(i+1, a[i]))       # Почему не работает? Научите, плз..


# Задание №2 (easy)

# people = ['Андрей', 'Антон', 'Алиса', 'Алексей', 'Анна', 'Александр']
# men = ['Андрей', 'Антон', 'Алексей', 'Александр']
# my_set = set(people)
# my_set2 = set(men)
# # people = list(my_set - my_set2)
# print(list(my_set - my_set2))


# Задание №3 (easy)

# numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# numbers2 = []
# for i in numbers:
#     if i%2 == 0:
#         i = i/4
#     else:
#         i = i*2
#     numbers2.append(i)
# print(numbers2)


# Задание №1 (normal)

# numbers = [2, -5, 8, 9, -25, 25, 4, 16, -16]
# numbers2 = []
# for i in numbers:
#     if i > 0:
#         i = i ** 0.5
#         if i.is_integer():
#             numbers2.append(int(i))
# print(numbers2)

# Задание №2 (normal)

# days = {
#         '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое',
#         '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое',
#         '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое',
#         '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
#         '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое',
#         '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
#         '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'
#         }
# months = {
#         '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
#         '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
#
#        }
#
# date = input('Введите дату в формате dd.mm.yyyy: ').split('.')
# while True:
#     if int(date[0]) < 1 or int(date[0]) > 31 or int(date[1]) < 1 or int(date[1]) > 12 or int(date[2]) <= 0:
#         print('Вы ввели некорректную дату.')
#         date = input('Введите дату в формате dd.mm.yyyy: ').split('.')
#     else:
#         break
# d = 0
# m = 0
# for key in days:
#     if key == date[0]:
#         d = days[key]
#         break
# for key in months:
#     if key == date[1]:
#         m = months[key]
#         break
# print(d, m, date[2], 'года')


# Задание №3 (normal)

# import random
#
# n = int(input('Сколько хотите элементов? '))
# a = []
# b = 0
# i = 1
# while i <= n:
#     b = random.randint(-100, 100)
#     a.append(b)
#     i += 1
# print(a)


# Задание №4 (normal)

# lst = [2, 5, 5, 6, 3, 9, 10, 2, 16]
# print(list(set(lst)))


# lst = [2, 5, 5, 6, 3, 9, 10, 2, 16]
# lst2 = []
# for i in lst:
#     n = lst.count(i)
#     if n == 1:
#         lst2.append(i)
# print(lst2)











