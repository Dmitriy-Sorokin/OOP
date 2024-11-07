# class SingletonFive:
#     __instance = None
#     __count = 0
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__count < 5:
#             cls.__instance = super().__new__(cls)
#             cls.__count += 1
#         return cls.__instance
#
#     def __init__(self, data):
#         self.name = data
# class Factory:
#
#     def build_sequence(self):
#         lst = []
#         return lst
#
#     def build_number(self, string):
#         result = float(string)
#         return result
#
# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
# ld = Loader()
# res = ld.parse_format("4, 5, -6.5", Factory())
#
# print(res)
import random
from traceback import print_tb

import requests
from jinja2.nodes import Slice


# class Car:
#
#     def __init__(self):
#         self.__model = ''
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if type(model) == str and 2 < len(model) < 100:
#             self.__model = model


# d = [{'ProviderName': '[251] - Autotests_BO', 'Country': 'BY', 'GameName': 'Caishen Gold: Dragon Awakes', 'Players': 2,
#       'Sessions': 196, 'Rounds': 310, 'Currency': 'BYN', 'TotalBet': 43327.2, 'TotalWin': 31638.0, 'GGR': 11689.2,
#       'TotalBetInEur': 12372.97, 'TotalWinInEur': 9034.88, 'GGRInEur': 3338.09, 'RTP': 73.02},
#      {'ProviderName': '[251] - Autotests_BO', 'Country': 'RU', 'GameName': 'Caishen Gold: Dragon Awakes', 'Players': 1,
#       'Sessions': 3, 'Rounds': 9, 'Currency': 'BYN', 'TotalBet': 1230.0, 'TotalWin': 367.5, 'GGR': 862.5,
#       'TotalBetInEur': 351.25, 'TotalWinInEur': 104.95, 'GGRInEur': 246.3, 'RTP': 29.88}]
# tuples = []
# for item in d:
#     tuples.append(list(item.values()))
#
# print(tuples)
#
# res = []
# for lst in tuples:
#     for i in lst:
#         if type(i) in (float, int):
#             r = tuples[0][lst.index(i)] + tuples[1][lst.index(i)]
#             res.append(r)
# print(res)
# count = 0
# for key, values in d[0].items():
#     if type(values) in (float, int):
#         d[0][key] = res[count]
#
#         count += 1
#
# print(d[0])


# def __setattr__(self, key, value):
#     if key == 'MIN_DIMENSION' or key == 'MAX_DIMENSION':
#         raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#     else:
#         return object.__setattr__(self, key, value)


# class AppVK:
#     def __init__(self):
#         self.name = "ВКонтакте"
#
# class AppYouTube:
#     def __init__(self, memory_max):
#         self.memory_max = memory_max
#         self.name = 'YouTube'
#
# class AppPhone:
#     def __init__(self, phone_list: dict):
#         self.name = 'Phone'
#         self.phone_list = phone_list

# class Module:
#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
#
#     def add_lesson(self, lesson):
#         self.lessons.append(lesson)
#
#     def remove_lesson(self, indx):
#         self.lessons.pop(indx)
#

# class LessonItem:
#     dct = {'title': str, 'practices': (int, float), 'duration': (int, float)}
#
#     def __init__(self, title, practices, duration):
#         self.title = title
#         self.practices = practices
#         self.duration = duration
#
#     def __delattr__(self, item):
#         if item in ('title', 'practices', 'duration'):
#             raise AttributeError("Атрибут id удалять запрещено.")
#         else:
#             object.__delattr__(self, item)
#
#     def __setattr__(self, key, value):
#         if not isinstance(value, self.dct[key]):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         if key == 'practices' and value <= 0:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         if key == 'duration' and value <= 0:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             return object.__setattr__(self, key, value)
#
#     def __getattr__(self, key):
#         return False

# class Handler:
#     def __init__(self, methods):
#         self.methods = methods
#
#     def __call__(self, func):
#         def wrapper(request, *args, **kwargs):
#             method = request.get('method')
#             if method in self.methods:
#                 return self.__getattribute__(method.lower())(func, request)
#             elif not method:
#                 return self.get(func, request)
#             else:
#                 return None
#
#         return wrapper
#
#     def get(self, func, request, ):
#         return f'GET: {func(request)}'
#
#     def post(self, func, request, ):
#         return f'POST: {func(request)}'


# @Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
# def contact(request):
#     return "Сергей Балакирев"
#
#
# res = contact({"method": "POST", "url": "contact.html"})

# class TicTacToe:
#     win_coord = {
#         1: [(0, 0), (0, 1), (0, 2)],
#         2: [(1, 0), (1, 1), (1, 2)],
#         3: [(2, 0), (2, 1), (2, 2)],
#         4: [(0, 0), (1, 0), (2, 0)],
#         5: [(0, 1), (1, 1), (2, 1)],
#         6: [(0, 2), (1, 2), (2, 2)],
#         7: [(0, 0), (1, 1), (2, 2)],
#         8: [(0, 2), (1, 1), (2, 0)]
#     }
#
#
#     def __init__(self):
#         self.pole = None
#         self.FREE_CELL = 0  # свободная клетка
#         self.COMPUTER_O = 2  # нолик (игрок - компьютер)
#         self.HUMAN_X = 1  # крестик (игрок - человек)
#
#     def init(self):
#         self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
#
#     def show(self):
#         for i in self.pole:
#             for j in i:
#                 if isinstance(j, Cell):
#                     print(j.value, end=' ')
#                 else:
#                     print(j, end=' ')
#             print()
#
#     def __getitem__(self, item):
#         self.__check(item)
#         x, y = item
#         if isinstance(self.pole[x][y], Cell):
#             return self.pole[x][y].value
#         else:
#             return self.pole[x][y]
#
#     def __setitem__(self, key, value):
#         self.__check(key)
#         x, y = key
#         self.pole[x][y] = value
#
#     def __check(self, coords):
#         if any(x not in range(3) for x in coords if not isinstance(x, slice)):
#             raise IndexError('некорректно указанные индексы')
#
#     def human_go(self):
#         while True:
#             x, y = map(int, input('Ваш ход: ').split())
#             if self[x, y] == self.FREE_CELL:
#                 self[x, y] = self.HUMAN_X
#                 break
#             else:
#                 print('Клетка занята, посмотрите еще раз')
#
#     def computer_go(self):
#         while True:
#             x = random.randint(0, 2)
#             y = random.randint(0, 2)
#             if self[x, y] == self.FREE_CELL:
#                 self[x, y] = self.COMPUTER_O
#                 break
#             else:
#                 # if self.is_draw:
#                 #     print('Ничья')
#                 #     break
#                 print('Клетка занята, посмотрите еще раз')
#
#
#     @property
#     def is_human_win(self):
#         for i in self.win_coord.values():
#             if all(self[x, y] == self.HUMAN_X if not isinstance(self[x, y], Cell) else False for x, y in i ):
#                 print('Вы выиграли')
#
#                 return True
#
#     @property
#     def is_computer_win(self):
#         for i in self.win_coord.values():
#             if all(self[x, y] == self.COMPUTER_O if not isinstance(self[x, y], Cell) else False for x, y in i ):
#                 print('Вы проиграли')
#                 return True
#
#     @property
#     def is_draw(self):
#         if all(self[x, y] != self.FREE_CELL for x in range(3) for y in range(3)):
#             print('Ничья')
#             return True
#
#     def __bool__(self):
#         if self.is_human_win or self.is_computer_win or self.is_draw:
#             return False
#         else:
#             return True
#
#
# class Cell:
#     def __init__(self):
#         self.value = 0
#
#     def __bool__(self):
#         return self.value == 0
#
#
#
# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")

# class Main:
#     def __init__(self, id=None, name=None, price=None, weight=None, dims=None, memory=None, frm=None):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.weight = weight
#         self.dims = dims
#         self.memory = memory
#         self.frm = frm


# class Thing:
#     _id = 0
#
#     def __init__(self, name, price):
#         self.id = Thing._id
#         Thing._id += 1
#         self.name = name
#         self.price = price
#         self.weight = None
#         self.dims = None
#         self.memory = None
#         self.frm = None
#
#     def get_data(self):
#         return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)
#
#
# class Table(Thing):
#     def __init__(self, name, price, weight, dims):
#         super().__init__(name, price)
#         self.weight = weight
#         self.dims = dims
#
#
# class ElBook(Thing):
#     def __init__(self, name, price, memory, frm):
#         super().__init__(name, price)
#         self.memory = memory
#         self.frm = frm
#
#
#
#
#
#
#
# table = Table("Круглый", 1024, 812.55, (700, 750, 700))
# book = ElBook("Python ООП", 2000, 2048, 'pdf')
#
# print(*table.get_data())
# print(*book.get_data())

















