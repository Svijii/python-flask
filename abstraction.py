from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
class Triangle(polygon):
    def sides(self):
        print(" I have 3 sides")
class square(polygon):
    def sides(self):
        print("I have 4 sides")
object1 = Triangle()
object1.sides()
object2 = square()
object2.sides()
