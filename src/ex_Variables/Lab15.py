# a = 5
# def sum():
#     b = 10
#     print(b)
# print(a)
# sum()

# a = 5
# def sum():
#     print(a)
# print(a)
# sum()

# a = 5
# def sum():
#     a =a+2
#     print(a)
# print(a)
# sum()

# a = 5
# def sum():
#     global a
#     a = a+2
# print(a)
# sum()
# print(a)

# def foo():
#     x = 20
#     def bar():
#         global x
#         x = 25
#         #print(x)
#     print("Before calling bar: ", x)
#     print("Calling bar now")
#     bar()
#     print("After calling bar: ", x)
# #(x)
# foo()
# print("x in main: ", x)

#Non-local Variable:
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()

# def A():
#     print("How are you")
#     def B():
#         print("hello world")
#     print("Nested function is executing")
#     B()
# A()

# def addtwonumbers(a,b):
#     #a=10
#     #b=20
#     c=a+b
#     print(c)
# addtwonumbers(100,10)

def oddoreven(num):
    #num=4
    if num % 2 == 0:
        print(num, "is even number")
    else:
        print(num, "is odd number")
oddoreven(4)
oddoreven(9)