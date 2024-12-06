# a = 5
# b = 0
# result = a/b
# print(result)
# print("Hello World")

# a = 5
# b = 0
# try:
#     result = a/b
#     print(result)
# except ZeroDivisionError as e:
#     print("Error handeled:", e)
# print("Hello World!")

# a = 5
# b = 0
# try:
#     result = a/b
#     print(result)
# except ZeroDivisionError as e:
#     print("Error handeled: ", e)
# except TypeError as e1:
#     print("type", e1)
# except ValueError as e3:
#     print("value", e3)
# print("Hello World!")

# a = 5
# b = 'a'
# try:
#     result = a/int(b)
#     print(result)
# except ZeroDivisionError as e:
#     print("Error handeled: ", e)
# except TypeError as e1:
#     print("type: ", e1)
# except ValueError as e3:
#     print("value: ", e3)
# print("Hello World!")

# import sys
# randomList = ['a', 0, 2]
# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1 / int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occured")
#         print("Next entry")
#         print()
# print("The reciprocal of", entry, "is", r)

# try:
#     num = int(input("Enter the number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)

# try:
#     f = open("test.txt", encoding = 'cp1252')
# finally:
#     f.close()

class InvalidageException(Exception):
    pass
class License(InvalidageException):
    age = 14
    if age >= 18:
        print("eligible")
    else:
        try:
            raise InvalidageException("Age is not valid")
        except InvalidageException as e:
            print(e)
