# Двусвязный список
class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            prev_tail = self.tail.get_prev()
            prev_tail.set_next(None)
            self.tail = prev_tail

    def get_data(self):
        result = []
        current = self.head
        while current:
            result.append(current.get_data())
            current = current.get_next()
        return result


class ObjList:
    def __init__(self, data, __next=None, __prev=None):
        self.__data = data
        self.__next = __next
        self.__prev = __prev

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data




# односвязный список

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        self.__data = obj


class Stack:

    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        h = self.top
        if h is None:
            return
        while h.next != self.last:
            h = h.next
        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None
        return last


    def get_data(self):
        result = []
        current = self.top
        while current:
            result.append(current.lst_math)
            current = current.next
        return result


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()  # ['obj1', 'obj2']
print(res)
