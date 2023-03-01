class StaticClass:

   @staticmethod # пометили метод декоратором
   def bar():
           print("bar")


StaticClass.bar() # вызов метода от класса

sm = StaticClass() # вызов метода из объекта
sm.bar()
#---------------------------------------------------------------------------------------------------------------------
class FiguresFactory:
  @staticmethod
  def createFugure(type, bounding_rect):
     if type == Square:
        #create square object
     if type == Elipse:
        #create elipse object
        #...
#-----------------------------------------------------------------------------------------------------------------------
        class SquareFactory:

            @staticmethod
            def create_square(self, side):
                return Square(side)