class Geek:
    def __init__(self,name,branch):
        self._name = name
        self.__branch = branch
    def display(self):
        print(self._name)
        print(self.__branch)
   # def __pop(self):
        #print(self.__branch)
    def access(self):
       print (self.__branch )






obj = Geek("Anitha","cse")
obj.access()


