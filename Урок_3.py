# Задание №1 (easy)

# вариант А

# def our_person(name, age, city):
#     person = '{}, {} лет, проживает в городе {}'.format(name, age, city)
#     return person
#
# name = input('Введите Ваше имя: ')
# age = input('Введите Ваш возраст: ')
# city = input('Введите город Вашего проживания: ')
#
# person = our_person(name, age, city)
# print(person)


# вариант В (без 'input' и с окончанием)

# def render_person(name, age, city):
#     if str(age)[-1] == '1' or age == 11:
#         a = 'год'
#     elif str(age)[-1] in ('2', '3', '4'):
#         a = 'года'
#     else:
#         a = 'лет'
#     print(name, age, a+',', 'проживает в городе', city)
# render_person('Олег,', 22, 'Жуковский')


# Задание №2 (easy)

# Вариант А

# def max_number(a, b, c):
#     my_num = [a, b, c]
#     max_num = (max(my_num))
#     return max_num
#
# a = int(input('Введите число: '))
# b = int(input('Еще число: '))
# c = int(input('И еще число: '))
#
# max_num = max_number(a, b, c)
# print(max_num)

# Вариант В

# def max_number(a, b, c):
#     return max(a, b, c)
# print(max_number(-5, -8, -145))


# Задание №3 (easy)

#Вариант А

# def max_str(*args):
#     max_len = max(*args, key=len)
#     return max_len
#
# arg_1 = input('Введите фразу: ')
# arg_2 = input('Добавьте к ней еще одну: ')
# arg_3 = input('Завершите трехстрочие: ')
#
# print('Это самая длинная фраза из трех - ', max_str(arg_1, arg_2, arg_3))


# Вариант В

# def max_str(*args):
#     max_len = max(*args, key=len)
#     print(max_len)
#
# max_str('rtyyu', 'hhhhhhhhh', 'tt', 'прроо')



# Задание №1 (normal?)

# names = ['Василий', 'Евгений', 'Катерина', 'Дмитрий']
# salaries = [300000, 78000, 430000, 6700000]
# result = dict(zip(names, salaries))
# for name, salary in result.items():
#     if salary > 500000:
#         continue
#     else:
#         with open('salary.txt', 'a') as file:
#             file.write('{} - {}\n'.format(name, salary))

# with open('salary.txt') as file:
#     for line in file:
#         b = line.split(' - ')
#         c = int(b[1]) * 0.87
#         print(b[0].upper(),'-', c)











