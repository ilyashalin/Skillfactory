class ParentClass:

    # метод, помещённый @classmethod - первый аргумент cls - модель класса
    # имя которого будет выводиться на печать при вызове
    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    # этот метод будет заменяться в дочернем классе
    @classmethod
    def call_original_method(cls):
        cls.method(5)

    # это обычный метод
    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    # метод, заменяющий метод родительского класса
    @classmethod
    def call_original_method(cls):
        cls.method(6)


# Вызываем методы класса через класс.
ParentClass.method(0)  # ParentClassclassmethod. 0
ParentClass.call_original_method()  # ParentClassclassmethod. 5

ChildClass.method(0)  # ChildClassclassmethod. 0
ChildClass.call_original_method()  # ChildClassclassmethod. 6

# Вызываем методы класса через объект.
my_obj = ParentClass()
my_obj.method(1)  # ParentClassclassmethod. 1
my_obj.call_class_method()  # ParentClassclassmethod. 10
