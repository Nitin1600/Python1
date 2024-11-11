# #write operation
# f = open("data.txt", 'w', encoding = "cp1252")
# f.write("this is write operation\n")
# f.write("this is second write operation")
# f.close()
#
# #read operation
# f = open("data.txt", "r")
# print(f.read())
# f.close()
#
# ##try, finally:
# try:
#     f = open("data.txt", "r", encoding="cp1252")
#     print(f.read())
# finally:
#     f.close()
#
# ##with open method:
# with open("data.txt", "r") as f:
#     print(f.read())

#with operation write:
# with open("data.txt", "a") as f:
#     f.write("This is operation \n")
#     f.write("This is with second operation \n")
#     f.write("This is with third operation \n")
#     f.close()
#
# #To print cursor position:
# with open("data.txt", "r") as f:
#     print(f.tell())
#     print(f.seek(10))
#     print(f.read())
#     f.close()

##read operation:
# with open("data.txt", "r") as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.read(10))
#     print(f.tell())
#     f.close()

##readline operation:
# with open("data.txt", "r") as f:
#     print("1 line => ", f.readline())
#     print("2 line => ", f.readline())
#     print("3 line => ", f.readline())
#     print("4 line => ", f.readline())
#     f.close()

##readlines:
# with open("data.txt", "x") as f:
#     f.write("this is my exclusive creation")
#     f.close()

##handle file exception:
try:
    with open("data.txt", "x") as f:
        f.write("this is my exclusive creation")
        f.close()
except FileExistsError:
    print("File already exists")