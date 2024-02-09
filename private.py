class employee():
    def __init__(self,name,empid):
        self.__name= name
        self.__empid= empid

    def __display(self):
        print(self.__name)
        print(self.__empid)
    def show(self):
        self.__display()


object = employee("viji",11465)
object.show()
