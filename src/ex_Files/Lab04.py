# f = open("test.txt")
# f = open("C:/Users/nitingpa/test.txt")

# f = open("test.txt", mode='r', encoding='cp1252')

# with open("test.txt",'w', encoding='cp1252') as f:
#     f.write("my first file\n")
#     f.write("This file\n\n\n")
#     f.write("This file contains three lines\n")

f=open("test.txt", 'r', encoding='cp1252')
f.read(4)
f.read(4)
f.tell()
f.seek(0)
# print(f.read())

# for line in f:
#     print(line, end="")
#     f.readline()
f.readlines()
