class SomeClass:
    def __init__(self, someData) -> None:
        # мы сохраняем переданные в конструкторе класса данные в поле internalData
        self.internalData = someData


if __name__ == "__main__":
    someObj = SomeClass(5)
    # как видно мы довольно легко можем получить доступ к внутренним данным класса
    # что не слишком-то хорошо
    print(someObj.internalData)
#----------------------------------------------------------------------------------------------------------------------
# Декоратор @property позволяет организовывать класс так, чтобы скрыть внутреннюю структуру класса от посторонних глаз
# (насколько это возможно) и оставить видимым только нужный API.
class SomeClass:
    def __init__(self, someData) -> None:
        self.__internalData = someData

    @property
    def data(self):
        return self.__internalData

    @data.setter  # так обозначается сеттер на поле data
    def data(self, value):
        self.__internalData = value


if __name__ == "__main__":
    someObj = SomeClass(5)
    # print(someObj.__internalData) # если мы попытаемся получить доступ к данным напрямую
    # то получим сообщение об ошибке

    print(someObj.data)  # выведет 5

    someObj.data = 10  # всё правильно
    print(someObj.data)  # выведет 10
#---------------------------------------------------------------------------------------------------------------------
# класс, который представляет собой значение угла
class Angle:
  def __init__(self, angle = 0) -> None:
      self.__angle = angle

  @property
  def angle(self):
     return self.__angle

  @angle.setter
  def angle(self, angle):
     self.__angle = angle


  #свойство, которое возвращает значение угла в радианах
  @property
  def rad(self):
     return (self.__angle/180.0)*3.14

if __name__ == "__main__":
  angle = Angle(30)
# выводим значение угла в угловых и радиальных значениях
  print(f'{angle.angle} : {angle.rad}')
# angle — доступное и для чтения, и для записи, которое позволяет работать с углом в градусах.
# rad — доступное только для чтения, которое позволяет получить значение угла в радианах.
# При этом если попытаться установить поле rad.