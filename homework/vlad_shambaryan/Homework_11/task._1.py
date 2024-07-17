class Book:
    # атрибуты для всех книг
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        # атрибуты для каждой книги
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def details(self):

        details = f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}"
        if self.reserved:
            details += ", зарезервирована"
        return details


book1 = Book("Идиот", "Достоевский", 500, "1234567890")
book2 = Book("Война и мир", "Толстой", 1300, "1234567891")
book3 = Book("Преступление и наказание", "Достоевский", 600, "1234567892")
book4 = Book("Мастер и Маргарита", "Булгаков", 400, "1234567893", reserved=True)
book5 = Book("Анна Каренина", "Толстой", 800, "1234567894")


books = [book1, book2, book3, book4, book5]
for book in books:
    print(book.details())


class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, subject, grade, has_exercises, reserved=False):

        super().__init__(title, author, pages, isbn, reserved)
        # атрибуты для школьных учебников
        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises

    def details(self):

        details = (f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages},"
                   f" предмет: {self.subject}, класс: {self.grade}")
        if self.reserved:
            details += ", зарезервирована"
        return details


school_book1 = SchoolBook("Алгебра", "Иванов", 200, "2234567890",
                          "Математика", 9, True)
school_book2 = SchoolBook("История", "Петров", 250, "2234567891",
                          "История", 10, False)
school_book3 = SchoolBook("География", "Сидоров", 150, "2234567892",
                          "География", 8, True, reserved=True)
school_book4 = SchoolBook("Физика", "Кузнецов", 300, "2234567893",
                          "Физика", 11, True)
school_book5 = SchoolBook("Химия", "Васильев", 220, "2234567894",
                          "Химия", 9, True)


school_books = [school_book1, school_book2, school_book3, school_book4, school_book5]
for school_book in school_books:
    print(school_book.details())
