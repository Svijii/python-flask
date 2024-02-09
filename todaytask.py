class student():
    def __init__(self,name,age):
        self.name = name
        self._age = age
    def get_age(self):
        return self._age
person = student("Anitha",22)
print(person.get_age())

