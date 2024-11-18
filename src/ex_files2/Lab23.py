# f = open("test.txt3", encoding="cp1252")
# f.close()

# try:
#     f=open("test.txt", encoding="cp1252")
# finally:
#     f.close()

# with open("text4.txt", "w", encoding="cp1252") as f:
#     f.write("This is first line \n")
#     f.write("This is second line \n\n")
#     f.write("This is third line \n")
#     f.close()

f=open("text4.txt", "r", encoding="cp1252")
f.read(4)
f.read(4)
f.read()
f.read()
f.tell()
f.seek(0)
# print(f.read())
# for line in f:
#     print(line, end="")
f.readline()
f.readline()
f.readline()
f.readlines()