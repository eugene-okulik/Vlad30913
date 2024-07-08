
my_dict = {
    'tuple': (1, 'two', None, True, 5.5),
    'list': ['apple', 'banana', 'cherry', 'lemon', 'kiwi'],
    'dict': {
        'brand': 'lexus',
        'model': 'rx 350',
        'year': '2009',
        'color': 'black',
        'max_speed': '200 km/h'
    },
    'set': {'blue', 'red', 'green', 'yellow', 'brown'}
}

print(my_dict['tuple'][-1])  # вывод на экран последний элемент

my_dict['list'].append("ananas")  # добавить в конец списка еще один элемент
my_dict['list'].pop(1)  # удалить второй элемент списка

my_dict['dict']['i am a tuple'] = 'False'  # добавьте элемент с ключом ('i am a tuple') и любым значением
my_dict['dict'].pop('color')  # удалить элемент

my_dict['set'].add('silver')  # добавить новый элемент в множество
my_dict['set'].remove('brown')  # удалить элемент из множества

print(my_dict)
