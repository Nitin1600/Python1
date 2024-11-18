class Animal:
    def __init__(self,name,importance):
        self.name=name
        self.importance=importance
    def PrintDetails(self):
        print(self.name,self.importance)
obj1=Animal("Tiger,","It's our national animal")
obj2=Animal("Dog,", "We pet it")
obj1.PrintDetails()
obj2.PrintDetails()

class Bike:
    def __init__(self,name,color,brand):
        self.name=name
        self.color=color
        self.brand=brand
    def PrintDetails(self):
        print(self.name,self.color,self.brand)
obj1=Bike("NS200,","White","Pulsar")
obj2=Bike("Splendor,","red,","Hero")
obj1.PrintDetails()
obj2.PrintDetails()