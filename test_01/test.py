# from test_01.input_field import InputField
#
#
# class TestInputField:
#     input_field = InputField()
#
#     def test_get_value(self):
#         self.input_field.text = "Test Value"
#         assert self.input_field.get_value() == "Test Value"
#
#     def test_set_value(self):
#         self.input_field.set_value("New Value")
#         assert self.input_field.text == "New Value"
#
#     def test_clear(self):
#         self.input_field.text = "Test Value"
#         self.input_field.clear()
#         assert self.input_field.text == ""
#
# a = [{'Row': 1, 'Column': 0}, {'Row': 1, 'Column': 1}, {'Row': 1, 'Column': 2}]
# b = [{'Row': 1, 'Column': 0}, {'Row': 1, 'Column': 2}, {'Row': 1, 'Column': 1}]
#
# # Sort the lists of dictionaries
# a_sorted = sorted(a, key=lambda x: (x['Row'], x['Column']))
# b_sorted = sorted(b, key=lambda x: (x['Row'], x['Column']))


# class Person:
#     def __init__(self, fio, job, old,  salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
#         self.lst = list(self.__dict__)
#
#     def __getitem__(self, item):
#         if item < 0 or item > 4:
#             raise IndexError('неверный индекс')
#         return self.__dict__[self.lst[item]]
#
#     def __setitem__(self, key, value):
#         if key < 0 or key > 4:
#             raise IndexError('неверный индекс')
#         self.__dict__[self.lst[key]] = value
#
#
#     def __iter__(self):
#         self.value = -1
#         return self
#
#     def __next__(self):
#         if self.value < 4:
#             self.value += 1
#             return self.__dict__[self.lst[self.value]]
#         else:
#             raise StopIteration


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print([x + y for x, y in zip(a, b)])