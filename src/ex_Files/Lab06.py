# #write operation:
# f = open("data2.txt", "w")
# f.write("This is my first line \n")
# f.write("This is my second line \n")
# f.write("This is my third line")
# f.close
#
# #using read method:
# f = open("data2.txt", "r")
# print(f.read())
# f.close()

#using for loop:
# f = open("data2.txt", "r")
# for line in f:
#     print(line, end="")
# f.close()

#using try and finally:
# try:
#     f = open("data2.txt", "r")
#     print(f.read())
# finally:
#     f.close()

#with statement:
# with open("data2.txt", "r", encoding="cp1252") as f:
#     print(f.read())

#using read method:
# with open("data2.txt", "r", encoding="cp1252") as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.tell())
#     f.seek(0)
#     print(f.read())

#using readline method:
# with open("data2.txt", "r", encoding="cp1252") as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.tell())
#     f.seek(0)
#     print(f.readlines())

##using append:
with open("data2.txt", "a", encoding="cp1252") as f:
    f.write("\nThis is my fourth line")

#Using exclusive creation:
with open("data3.txt", "x", encoding="cp1252") as f:
    f.write("\nThis is my fourth line")