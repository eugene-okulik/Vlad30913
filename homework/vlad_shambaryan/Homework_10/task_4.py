PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split('\n')

price_dict = {x.split()[0]: int(x.split()[1][:-1]) for x in new_list}
print(price_dict)
