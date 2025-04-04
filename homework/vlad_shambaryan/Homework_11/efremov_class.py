
class MyClass:
    x = 5
print(MyClass)
p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Vlad', 46)
print(p1.name)
print(p1.age)
print(p1.name, p1.age)
#===================================================
class Person:
    def __init__(self, name, age):# inicializator
        self.name = name
        self.age = age

    def myfunc(man):
        print("Меня зовут", man.name, "Мне", man.age,"полных лет" )

p1 = Person('Vlad', 46)
p1.myfunc()

p1.age = 40
# del p1.age
print(p1.name)
p1.myfunc()
print(p1.name, p1.age)
#==================================================================

class Person:
    def __init__(self, fname, lname):
        self.f = fname
        self.l = lname

    def printname(man):
        print(man.f, man.l)

x = Person("Vlad", "sham")
x.printname()
#=======================================================================
class Person:
    def __init__(self, fname, lname):
        self.f = fname
        self.l = lname

    def printname(man):
        print(man.f, man.l)

class Students(Person):
    pass
x = Students("Miqos", "Sham")
x.printname()

#=======================================================================
class Person:
    def __init__(self, fname, lname):
        self.f = fname
        self.l = lname

    def printname(man):
        print(man.f, man.l)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)# zavisit ot classa Person

x = Student("Miqos", "Shamb")
x.printname()
#====================================================================
class Person:
    def __init__(self, fname, lname):
        self.f = fname
        self.l = lname

    def printname(man):
        print(man.f, man.l)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)# super oznachaet zavisit ot classa Person
        self.godrojdeniya = year

    def myfunc(man):
        print("Меня зовут", man.f, "Я", man.l, man.godrojdeniya )

x = Student("Miqos", "Shamb", 2014)
x.printname()
print(x.godrojdeniya)
x.myfunc()
#===================================================================
class Person:
    age = 10
    welcome = "школьник"
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(man):
        print(man.firstname, man.lastname, Person.welcome)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)# super oznachaet zavisit ot classa Person
        self.godrojdeniya = year

    def welcome(man):
        print("Меня зовут", man.firstname, man.lastname, "мне", Person.age, "я родился", man.godrojdeniya , "я", Person.welcome)

x = Student("Miqael", "Shambaryan", 2014)
x.printname()
print(x.godrojdeniya)
x.welcome()

