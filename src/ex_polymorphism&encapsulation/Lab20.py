# class India:
#     def capital(self):
#         print("New Delhi is the capital of India")
#
#     def language(self):
#         print("Hindhi is a widely spoken language")
#
#     def type(self):
#         print("India is a developing country")
#
# class USA:
#     def capital(self):
#         print("Washington D.C is the capital of India")
#
#     def language(self):
#         print("English is a widely spoken language")
#
#     def type(self):
#         print("USA is a developed country")
#
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
# obj_india = India()
# obj_usa = USA()
#
# func(obj_india)
# func(obj_usa)

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
# class Animal:
#     def speak(self):
#       raise NotImplementedError("Subclass must implement this method")
# class Dog(Animal):
#     def speak(self):
#       return "Woof!"
# class Cat(Animal):
#     def speak(self):
#          return "Meow!"
#
# # Create a list of Animal objects
# animals = [Dog(), Cat()]
#
# # Call the speak method on each object
# for animal in animals:
#     print(animal.speak())
