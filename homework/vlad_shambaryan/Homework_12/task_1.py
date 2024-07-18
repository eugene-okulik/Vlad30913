# базовый класс для всех цветов
class Цветок:
    def __init__(self, имя, цвет, длина_стебля, свежесть, цена, время_жизни):
        self.имя = имя
        self.цвет = цвет
        self.длина_стебля = длина_стебля
        self.свежесть = свежесть
        self.цена = цена
        self.время_жизни = время_жизни

    def __str__(self):
        return (f"{self.имя} ({self.цвет}) - свежесть: {self.свежесть}, длина стебля: {self.длина_стебля}, "
                f"цена: {self.цена}, время жизни: {self.время_жизни}")


# конкретные классы цветов
class Роза(Цветок):
    def __init__(self, цвет, длина_стебля, свежесть, цена, время_жизни):
        super().__init__("Роза", цвет, длина_стебля, свежесть, цена, время_жизни)


class Тюльпан(Цветок):
    def __init__(self, цвет, длина_стебля, свежесть, цена, время_жизни):
        super().__init__("Тюльпан", цвет, длина_стебля, свежесть, цена, время_жизни)


class Солнечник(Цветок):
    def __init__(self, цвет, длина_стебля, свежесть, цена, время_жизни):
        super().__init__("Солнечник", цвет, длина_стебля, свежесть, цена, время_жизни)


# класс Букет
class Букет:
    def __init__(self):
        self.цветы = []

    def добавить_цветок(self, цветок):
        self.цветы.append(цветок)

    def рассчитать_стоимость(self):
        return sum(цветок.цена for цветок in self.цветы)

    def рассчитать_время_жизни(self):
        return sum(цветок.время_жизни for цветок in self.цветы) / len(self.цветы)

    def сортировать_по(self, атрибут):
        self.цветы.sort(key=lambda цветок: getattr(цветок, атрибут))

    def поиск_по(self, атрибут, значение):
        return [цветок for цветок in self.цветы if getattr(цветок, атрибут) == значение]


# некоторые объекты цветов
роза1 = Роза("красный", 50, 90, 10, 7)
роза2 = Роза("розовый", 40, 80, 8, 5)
тюльпан1 = Тюльпан("желтый", 30, 70, 6, 3)
солнечник1 = Солнечник("оранжевый", 60, 95, 12, 10)

# букет и добавить цветы к нему
букет = Букет()
букет.добавить_цветок(роза1)
букет.добавить_цветок(роза2)
букет.добавить_цветок(тюльпан1)
букет.добавить_цветок(солнечник1)

# стоимость и время жизни букета
print(f"Стоимость букета: {букет.рассчитать_стоимость()} $")
print(f"Время жизни букета: {букет.рассчитать_время_жизни()} дней")

# цветы в букете по свежести
букет.сортировать_по("свежесть")
print("Сортировка по свежести:")
for цветок in букет.цветы:
    print(цветок)

# время жизни 5 дней
результат = букет.поиск_по("время_жизни", 5)
print("Цветы с временем жизни 5 дней:")
for цветок in результат:
    print(цветок)
