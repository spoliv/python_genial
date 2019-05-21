# 21.05.2019
# 
# 
# # Задание №1 (easy)
# 
# import os
# import sys
# import shutil
# 
# # a)
# 
# path_dir = [('dir_' + str(i + 1)) for i in range(9)]
# 
# 
# def make_dir(paths):
# 
#     dir_path = os.path.join(os.getcwd(), paths)
#     try:
#         os.mkdir(dir_path)
#     except:
#         print(dir_path + ' - заменить существующую?')
# #
# # # for i in path_dir:
# # #     make_dir(i)
# #
# # # b)
# 
# def remove_dir(paths):
# 
#     dir_path = os.path.join(os.getcwd(), paths,)
#     try:
#         os.rmdir(dir_path)
#     except:
#         print(dir_path + ' - не существует')
# #
# # # for i in path_dir:
# # #     remove_dir(i)
# #
# # # Задание №2 (easy)
# 
# def list_dir(main_path):
# 
#     for dir in os.listdir(main_path):
#         print(dir)
# # # main_path = os.getcwd()
# # # list_dir(main_path)
# #
# # # Задание №3 (easy)
# 
# def copy_file(first_file, new_file):
# 
#     shutil.copy(first_file, new_file)
# #
# # first_file = sys.argv[0]
# #     # print(first_file)
# # new_file = os.getcwd() + '\easy.py'
# #     # print(new_file)
# # copy_file(first_file, new_file)
# 
# def change_dir(dir_path):
# 
#     try:
#         os.chdir(dir_path)
#         print(os.getcwd() + ' - текущая директория')
#     except:
#         print(dir_path + ' - такой директории нет')
# 
# # Задание №1 (normal)
# 
# # import easy
# 
# choice = 'a'
# while choice != '0':
#     print('Перейти в папку - 1')
#     print('Просмотреть содержимое текущей папки - 2')
#     print('Удалить папку - 3')
#     print('Создать папку - 4')
#     print('Выход - 0')
#     choice = input('Выбрать: ')
#     print(choice)
# 
#     if choice == '1':
#         dir_name = input('наберите полный путь папки: ')
#         change_dir(dir_name)
#     elif choice == '2':
#         dir_name = os.getcwd()
#         list_dir(dir_name)
#     elif choice == '3':
#         dir_name = input('наберите полный путь папки: ')
#         remove_dir(dir_name)
#     elif choice == '4':
#         dir_name = input('наберите полный путь папки: ')
#         make_dir(dir_name)
#     elif choice == '0':
#         pass
#     else:
#         print('Не понял')
# 
# 
# # def rem(path):
# #    if os.path.isfile(path):
# #      os.remove(path)
# 
# 
# # print(os.getcwd())







