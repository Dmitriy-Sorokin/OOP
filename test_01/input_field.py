filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ('jpg', 'bmp', 'jpeg')

def foo(data_list, data_tuple):
    result = []
    for data in data_list:
        if data.split('.')[-1] in data_tuple:
            result.append(data)
    return result
print(foo(filenames, acceptor))
