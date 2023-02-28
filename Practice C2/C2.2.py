# Возможность объединять классы в иерархии. Это позволяет постепенно наращивать функциональность
# и более полно использовать уже написанный код.
# Например, иерархия объектов окружающего мира:
class Object:
  def __init__(self, name) -> None:
#поле name будет представлено в объектах этого класса
#и в объектах всех классов наследников
      self.name = name


#тоже относится и к методу getName(),
#который будучи однажды реализован не нужно будет уже повторять в дочерних классах
  def getName(self):
     return self.name


#В классе ФизическийОбъект добавим свойства вес и размер
class PhisicalObject(Object):
  def __init__(self, name, weight, size) -> None:
      super().__init__(name)
      self.weight = weight
      self.size = size

  def getWeight(self):
     return self.weight

  def getSize(self):
     return self.size


#классы живых и неживых объектов повторяют все поля и методы класса PhisicalObject(автоматически)
#и используются, чтобы разделить иерархию на две ветви
#от НеживыхОбъектов можно будет ввести иерархию в камни, металлы, газы и т.д
#а от живых — в Растения, Животные, Насекомые, Грибы и т.д.
class NonLivingObject(PhisicalObject):
  def __init__(self, name, weight, size) -> None:
     super().__init__(name,weight,size)

class LivingObject(PhisicalObject):
  def __init__(self, name, weight, size) -> None:
     super().__init__(name,weight,size)