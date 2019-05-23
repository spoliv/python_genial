# 22.05.2019

# Задание №1-2 (easy)

# class Car:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#
#     def car_go(self):
#         print('Машина {} начала движение.'.format(self.name))
#
#     def car_stop(self):
#         print('Машина {} остановилась.'.format(self.name))
#
#     def car_turn(self, direction):
#         print('Машина {} повернула {}.'.format(self.name, direction))
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_mechanical=False):
#         Car.__init__(self, speed, color, name)
#         self.is_mechanical = is_mechanical
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name):
#         Car.__init__(self, speed, color, name)
#
#     def car_go(self):
#         print('Машина {} рванула с места.'.format(self.name))
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name):
#         Car.__init__(self, speed, color, name)
#
#     def car_go(self):
#         print('Машина {} медленно тронулась.'.format(self.name))
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police=True):
#         Car.__init__(self, speed, color, name)
#         self.is_police = is_police


# my_car = PoliceCar(150, 'Azul', 'Volga')
# my_car.car_turn('куда-то')
# print()

# my_car = WorkCar(30, 'Green', 'МТЗ')
# my_car.car_go()
# print()

# my_car = TownCar(100, 'Yellow', 'Oka')
# print(my_car)

# my_car = SportCar(200, 'Orange', 'Всё таки')
# my_car.car_go()
# print()


# Задание №1(normal)

#class Toy:
#     def __init__(self, toy_type, color, name):
#         self.name = name
#         self.color = color
#         self.toy_type = toy_type
# 
#     def toy_purchase_materials(self):
#         print('Закупаем сырье для {}'.format(self.name))
# 
#     def toy_sewing(self):
#         print('Пошив {}'.format(self.name))
# 
#     def toy_coloring(self):
#         print('Красим {} в цвет {}'.format(self.name, self.color))
# 
#     def toy_make(self):
#         print('Создаем новую игрушку {}'.format(self.name))
#         self.toy_purchase_materials()
#         self.toy_sewing()
#         self.toy_coloring()
#         print('Новая игрушка {} создана!'.format(self.name))
# 
# new_toy = Toy('мягкий', 'коричневый', 'мишка')
# new_toy.toy_make()








