from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def regular_method(self):
        print("This is a regular method.")

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("This is the implementation of the abstract method.")

instance = ConcreteClass()
instance.abstract_method()
instance.regular_method()
