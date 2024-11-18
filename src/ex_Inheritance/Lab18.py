#Single level inheritance:
# class A:
#     pass
#
# class B(A):
#     pass

#Multiple inheritance
# class A:
#     pass
#
# class B:
#     pass
#
# class C(A,B):
#     pass

#Multilevel inheritance:
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass

#example1:
# class Student:
#     def printDetails(self):
#         print("Hello Raj goodmorning")
# class Main(Student):
#     pass
# obj=Main()
# obj.printDetails()

#example2:
#Multiple inheritance:
# class Student:
#     def printDetails(self):
#         print("Hello raja, good morning")
# class Address:
#     def printAddress(self):
#         print("I am from bengaluru")
# class Main(Student,Address):
#     pass
# obj=Main()
# obj.printDetails()
# obj.printAddress()

#Multilevel inheritance:
# class Student:
#     def printDetails(self):
#         print("Hello puneeth, good morning")
# class Address(Student):
#     def printAddress(self):
#         print("I am from andhra_pradesh")
# class Main(Address):
#     pass
# obj=Main()
# obj.printDetails()
# obj.printAddress()

##properties inheritance ex:
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printDetails(self):
        print(self.name,self.age)
class Address(Student):
    def __init__(self,name,age,address):
        self.address=address
        Student.__init__(self,name,age)
    def printFullDetails(self):
        print(self.name,self.age,self.address)
# class City(Address):
#     def __init__(self,name,age,address,city):
#         self.city=city
#         Address.__init__(self,name,age,address)
#     def printFullDetails1(self):
#         print(self.name,self.age,self.address,self.city)
class Main(Address):
    pass
obj1=Main("Raj","30","Vijaynagar")
obj2=Main("Puneeth","35","Banashankari")
# obj2.printDetails()
obj1.printFullDetails()
obj2.printFullDetails()