#write operation
f = open("data.txt", 'w', encoding = "cp1252")
f.write("this is write operation\n")
f.write("this is second write operation")
f.close()

#read operation
f = open("data.txt", "r")
print(f.read())
f.close()