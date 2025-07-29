class Person():
    cityname = "mumbai"
    def printname(self,name):
        print(name)
class Ashok(Person):
    def printdetail(self):
        print("intoduction to python")
obj = Ashok()
obj.cityname = "bangalore"
obj .printname("Ashok")
obj = Arun()
obj.cityname = "mumbai"
obj .printname("Arun")