# def my_gen():
#     n = 1
#     print("This is printed first")
#     yield n
#     n += 1
#
#     print("This is printed second")
#     yield n
#
#     n += 1
#     print("This is printed last")
#     yield n
#
# a = my_gen()
# print(next(a))
# print(next(a))
# print(next(a))
# # print(next(a))

# def my_gen():
#     n = 1
#     print("This is printed first")
#     yield n
#
#     n += 1
#     print("This is printed second")
#     yield n
#
#     n += 1
#     print("This is printed last")
#     yield n
#
# for item in my_gen():
#     print(item)

# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length  -1,-1,-1):
#         yield my_str[i]
#
# for char in rev_str("Nitin"):
#     print(char)

# my_list=[1,3,6,10]
# list_=[x**2 for x in my_list]
# generator=(x**2 for x in my_list)
# print(list_)
# print(generator)

# my_list=[1,3,6,10]
# # a=(x**2 for x in my_list)
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # next(a)
#
# print(sum(x**2 for x in my_list))
# print(max(x**2 for x in my_list))

# class PowTwo:
#     def __init__(self,max=0):
#         self.n=0
#         self.max=max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.n < self.max
#         raise StopIteration
#
#         result = 2 ** self.n
#         self.n += 1
#         return result

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


