class student():
    def __init__(self,age,rollno,name):
        self.__age = age
        self._rollno = rollno
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self):
        self.__name
    def get_age(self):
        return self.__age
    def set_age(self):
        self.__age
object=student(34,11564,"Anitha")
print(object.get_name())
print(object.get_age())

