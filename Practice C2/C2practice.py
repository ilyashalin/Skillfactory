#1) Создавайте все внутренние поля класса в конструкторе, так вы исключите возможность того,
# что какого-то поля не окажется в нужный момент.
class Miscast:
  def __init__(self) -> None:
      pass

  def setValue(self,value):
     self.value = value

  #если вызвать getValue, до того как было вызвано setValue,
  #возникнет исключение, поскольку поля value до этого отсутствует
  def getValue(self):
     return self.value

if __name__ == "__main__":
  mis = Miscast()
  mis.getValue()
#----------------------------------------------------------------------------------------------------------------------
#2) Делайте различия между общими (теми, которые имеют отношение к самому классу) и частными
# (те, которые имеют отношение к конкретному объекту) методами класса. Пользуйтесь для этого декоратором @classmethod.
class BankAccount:
    MIN_BALANCE = -10_000

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.created_at = datetime.now().date()

    # общий метод класса, который создает объект прочитывая соответствующий csv файл
    @classmethod
    def from_csv(cls, filepath):
        with open(filepath, "r") as f:
            row = csv.reader(f).__next__()
            owner, account_number = row
        return cls(owner, account_number)


if __name__ == "__main__":
    my_account = BankAccount.from_csv("testfile.csv")
    print(my_account._owner, my_account._account_number, my_account._balance)
#3) Определяйте операцию сравнения на равенство объектов, когда это имеет смысл, реализуя метод __eq__.
class Angle:
 def __init__(self, angle = 0) -> None:
     self.__angle = angle


 # метод __eq__ позволяет сравнивать объекты, используя оператор ==
 def __eq__(self, __o: object) -> bool:
     return self.__angle == __o.__angle

 @property
 def angle(self):
    return self.__angle

 @angle.setter
 def angle(self, angle):
    self.__angle = angle

if __name__ == "__main__":
  a1 = Angle(30)
  a2 = Angle(45)
  a3 = Angle(30)
  print(f'a1 == a2 -> {a1 == a2}')
  print(f'a1 == a3 -> {a1 == a3}')
#-----------------------------------------------------------------------------------------------------------------------
#4) Другим, похожим на __str__ методом, является метод __repr__.
# Его используют для того, чтобы получить строку создания объекта.
class Angle:
def __init__(self, angle = 0) -> None:
    self.__angle = angle

def __str__(self):
  return f"""Angle: value = {self.__angle}"""

def __repr__(self) -> str:
    return f"""Angle(angle={self.__angle})"""

@property
def angle(self):
   return self.__angle

@angle.setter
def angle(self, angle):
   self.__angle = angle

if __name__ == "__main__":
  a = Angle(30)
  print(a) # выведет Angle: value = 30
  print(repr(a)) #выведет Angle(angle=30)
#-----------------------------------------------------------------------------------------------------------------------
#5) Оформляйте статические методы при помощи @staticmethod. Это сделает ваш код более читабельным,
# а вашу идею при создании класса — более явной.
#6) Помечайте поля и методы: Одно нижнее подчеркивание — для внутреннего использования. “_” ничего не делает,
# но говорит внешним пользователям класса о том, что это поле или метод для «внутреннего» использования,
# не рекомендуя их использовать.
#7) Предоставляйте поля во внешний API при помощи декоратора @property.
#8) Cопровождайте свои методы и классы docstring.
class Angle:
# docstring — краткое описание класса, которое в дальнейшем может быть получено через поле __doc__
"""
   A class used to represent an angle.
   Attributes
   ----------
   angle : int
   rad : int (readonly)

   Methods
   -------
   normalize()
       gets angle value to range from 0 to 360
"""

def __init__(self, angle = 0) -> None:
    self.__angle = angle

@property
def angle(self):
   return self.__angle

@angle.setter
def angle(self, angle):
   self.__angle = angle

@property
def rad(self):
  return (self.__angle/180.0)*math.pi

def normalize(self):
  self.__angle = self.__angle % 360

if __name__ == "__main__":
  print(Angle.__doc__) #вывод на печать описания класса выше