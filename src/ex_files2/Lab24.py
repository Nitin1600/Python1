# #write operation:
# f=open("data4.txt", "w", encoding="cp1252")
# f.write("This is my write operation \n")
# f.write("This is my second write operation")
# f.close()

#read operation:
# f=open("data4.txt", "r")
# print(f.read())
# f.close()

#try & finally:
# try:
#     f=open("data4.txt", "r", encoding="cp1252")
#     print(f.read())
# finally:
#     f.close()

#with open method:
# with open("data4.txt", "r") as f:
#     print(f.read())

#with operation write:
# with open("data4.txt", "a") as f:
#     f.write("This is with operation \n")
#     f.write("This is with second operation \n")
#     f.write("THis is with third operation")
#     f.close()

#to print cursor position:
# with open("data4.txt", "r") as f:
#     print(f.tell())
#     print(f.seek(10))
#     print(f.read())
#     f.close()

#read opearion:
# with open("data4.txt", "r") as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.read(10))
#     print(f.tell())
#     f.close()

#readline operation:
# with open("data4.txt", "r") as f:
#     print("1st line is => ", f.readline())
#     print("2nd line is => ", f.readline())
#     print("3rd line is => ", f.readline())
#     print("4th line is => ", f.readline())
#     f.close()

#readlines
# with open("data4.txt", "x") as f:
#     print("This is my exclusive creation")
#     f.close()

#handle file exception:
# try:
#     with open("data4.txt", "x") as f:
#         f.write("This is my exclusive creation")
# except FileExistsError:
#     print("File is already exist")

