# a = 4
# if a < 3
#     print(a)

# print(1/0)
# open("imaginary.txt")
# print(dir(locals()['__builtins__']))

# import sys
# randomList = ['a',0,2]
# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info(), "entry")
#         print("Next entry")
#         print()
# print("The reciprocal of", entry, "is", r)

# import sys
# randomList = ['a',0,2]
# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break
#     except Exception as e:
#         print("Oops!", e.__class__, "Occured")
#         print("Next entry is")
#         print()
# print("The reciprocal of", entry, "is", r)

# try:
#     #do something
#     pass
# except ValueError:
#     #handle ValeError exception
#     pass
# except(ZeroDivisionError, TypeError):
#     #handle multiple exceptions
#     #handle ZeroDivisionError, TypeError
#     pass
# except:
#     #handle all other exceptions
#     pass

# raise KeyboardInterrupt
# raise MemoryError("This is an argument")

# try:
#     a = int(input("Enter the positive integer: "))
#     if a < 0:
#         raise ValueError("This is not a Positive number")
# except ValueError as ve:
#     print(ve)

# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number")
# else:
#     reciprocal = 1 / num
#     print(reciprocal)

# try:
#     f = open("test.txt", encoding='utf-8')
# finally:
#     f.close()