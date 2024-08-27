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
import math
import random
import sys
import time


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

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @a.setter
    def a(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__a = value
        else:
            raise ValueError("Значение должно быть в диапазоне от 10 до 10000")

    @b.setter
    def b(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__b = value
        else:
            raise ValueError("Значение должно быть в диапазоне от 10 до 10000")

    @c.setter
    def c(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__c = value
        else:
            raise ValueError("Значение должно быть в диапазоне от 10 до 10000")

    def __eq__(self, other):
        self_dim = self.a * self.b * self.c
        other_dim = other.a * other.b * other.c
        return self_dim == other_dim

    def __gt__(self, other):
        self_dim = self.a * self.b * self.c
        other_dim = other.a * other.b * other.c
        return self_dim > other_dim

    def __lt__(self, other):
        self_dim = self.a * self.b * self.c
        other_dim = other.a * other.b * other.c
        return self_dim < other_dim

    def __ge__(self, other):

        self_dim = self.a * self.b * self.c
        other_dim = other.a * other.b * other.c
        return self_dim >= other_dim

    def __le__(self, other):
        self_dim = self.a * self.b * self.c
        other_dim = other.a * other.b * other.c
        return self_dim <= other_dim


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

sorted_lst_shop = sorted(lst_shop, key=lambda x: x.dim.c * x.dim.b * x.dim.a)

for item in sorted_lst_shop:
    print(f"{item.name}: {item.price}")
