class employee():
    def __init__(self,name,empid):
        self._name= name
        self._empid= empid #protected instance variable

    def display(self):
        print(self._name)
        print(self._empid)

class male(employee):
    def __init__(self,name,empid):
        employee.__init__(self,name,empid)
    def show(self):
        print(self._name)
object = male("viji",11465,)
object.show()




