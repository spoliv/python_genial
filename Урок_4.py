# Задание №1 (easy)

# num = [2, 6, 5, 11, 25, 13]
# print('my_num - ', [i ** 2 for i in num])


# Задание №2 (easy)

# Вариант А (короче, по-моему)

# list_a = ['ананас', 'маракуйя', 'яблоко', 'абрикос', 'киви', 'апельсин']
# list_b = ['яблоко', 'груша', 'слива', 'апельсин', 'абрикос', 'вишня']
# print('my_list - ', list(set(list_a) & set(list_b)))

# Вариант В

# list_a = ['ананас', 'маракуйя', 'яблоко', 'абрикос', 'киви', 'апельсин']
# list_b = ['яблоко', 'груша', 'слива', 'апельсин', 'абрикос', 'вишня']
# print('my_list - ', [i for i in list_a if i in list_b])

# Задание №3 (easy)

# list = [67, 0, -33, 12, 135, -9, 45, 999]
# print('my_list - ', [num for num in list if num % 3 == 0 and num > 0 and num % 4 != 0])


# Задание №1 (normal)

# import re
# 
# pattern_name = '^[A-ZА-Я][a-zа-я]+$'
# pattern_surname = pattern_name
# pattern_email = '^[a-z_0-9]+@[a-z0-9]+\.(ru|org|com)$'
# 
# name = input('Введите имя с заглавной буквы: ')
# surname = input('Введите фамилию с заглавной буквы: ')
# email = input('Введите имейл в нижнем регистре: ')
# 
# result_name = re.match(pattern_name, name)
# result_surname = re.match(pattern_surname, surname)
# result_email = re.match(pattern_email, email)

        # if not result_name:                         #  еще вариант
        #     print('Имя введено некорректно ')
        # if not result_surname:
        #     print('Фамилия введена некорректно')
        # if not result_email:
        #     print('Email введен некорректно')

# if not result_name or not result_surname or not result_email:
#     print('Данные введены некорректно ')
# else:
#     print('Всё верно!')


# Задание №2 (normal)

# import re
#
# some_str = '''                                # немного сократил текст
# Мороз и солнце; день чудесный!
# Еще ты дремлешь, друг прелестный —
# Пора, красавица, проснись:
# Открой сомкнуты негой взоры
# Навстречу северной Авроры,
# Звездою севера явись!
# Вечор, ты помнишь, вьюга злилась,
# На мутном небе мгла носилась;
# Луна, как бледное пятно,
# Сквозь тучи мрачные желтела,
# И ты печальная сидела —
# А нынче... погляди в окно:
# Под голубыми небесами
# Великолепными коврами,
# Блестя на солнце, снег лежит;
# Прозрачный лес один чернеет,
# И ель сквозь иней зеленеет,
# И речка подо льдом блестит.'''
#
# pattern = '\.{2,}'
#
# result = re.search(pattern, some_str)
#
#
# if result:
#     print('В тексте есть более одной точки подряд.')
# else:
#     print('В тексте нет более одной точки подряд.')











