# базовый класс для всех цветов
class Flower:
    def __init__(self, name, color, stem_length, freshness, price, lifetime):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price
        self.lifetime = lifetime

    def __str__(self):
        return (f"{self.name} ({self.color}) - freshness: {self.freshness}, stem length: {self.stem_length},"
                f" price: {self.price}, lifetime: {self.lifetime}")


# конкретные классы цветов
class Rose(Flower):
    def __init__(self, color, stem_length, freshness, price, lifetime):
        super().__init__("Rose", color, stem_length, freshness, price, lifetime)


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, price, lifetime):
        super().__init__("Tulip", color, stem_length, freshness, price, lifetime)


class Sunflower(Flower):
    def __init__(self, color, stem_length, freshness, price, lifetime):
        super().__init__("Sunflower", color, stem_length, freshness, price, lifetime)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        return sum(flower.price for flower in self.flowers)

    def calculate_lifetime(self):
        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):
        self.flowers.sort(key=lambda flower: getattr(flower, attribute))

    def search_by(self, attribute, value):
        return [flower for flower in self.flowers if getattr(flower, attribute) == value]


# некоторые объекты цветов
rose1 = Rose("red", 50, 90, 10, 7)
rose2 = Rose("pink", 40, 80, 8, 5)
tulip1 = Tulip("yellow", 30, 70, 6, 3)
sunflower1 = Sunflower("orange", 60, 95, 12, 10)

# букет и добавить цветы к нему
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip1)
bouquet.add_flower(sunflower1)

# стоимость и время жизни букета
print(f"Стоимость букета: {bouquet.calculate_cost()} $")
print(f"Срок службы букета: {bouquet.calculate_lifetime()}")

# цветы в букете по свежести
bouquet.sort_by("freshness")
print("Сортировка по свежести:")
for flower in bouquet.flowers:
    print(flower)

# время жизни 5 дней
result = bouquet.search_by("lifetime", 5)
print("Цветы со сроком жизни 5 дней.:")
for flower in result:
    print(flower)
