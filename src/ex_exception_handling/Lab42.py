# a = 10
# b = 'a'
# try:
#     result = a/int(b)
#     print(result)
# except ZeroDivisionError as e:
#     print("Error handeled:", e)
# except TypeError as e1:
#     print("TypeError:", e1)
# except ValueError as e2:
#     print("ValueError", e2)
# except Exception as e4:
#     print("Error details", e4)
# print("Hello World")
#
# try:
#     f = open("test.txt", encoding='cp1252')
#     print(f)
# except FileNotFoundError as e5:
#     print("File Details:", e5)

class InvalidageException(Exception):
    """age is not valid"""
class License(InvalidageException):
    age = 14
    if age >= 18:
        print("Eligible")
    else:
        try:
            raise InvalidageException("age is not valid")
        except InvalidageException as e:
            print("Eligibility:", e)