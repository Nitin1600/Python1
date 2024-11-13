# numbers = [6,5,3,8,4,2,5,4,11]
# sum = 0
# for val in numbers:
#     sum = sum+val
# print("The sum is: ", sum)

# print(range(10))
# print(list(range(10)))
# print(list(range(2,8)))
# print(list(range(2,20,3)))

# genre = ["pop", "rock", "jazz"]
# for i in range(len(genre)):
#     print("I like",genre[i])

# digits = [0,1,5]
# for i in digits:
#     print(i)
# else:
#     print("No items left")

# n = int(input("Enter n:"))
# sum = 0
# i = 1
# while i >= n:
#     sum = sum - i
#     i = i - 1
# print("The sum is:",-sum)

# counter = 0
# while counter < 3:
#     print("inside loop")
#     counter = counter + 1
# else:
#     print("inside else")

# for val in "String":
#     if val=="i":
#         break
#     print(val)

# for val in "String":
#     if val == "i":
#         continue
#     print(val)

# num = 5
# if num > 0:
#     print(num, "is a positive number")

# num = -5
# if num > 0:
#     print(num, "is a positive number")
# else:
#     print(num, "is a negative number")

num = -5
if num >= 0:
    if num == 0:
        print(num, "is a Zero")
    else:
        print(num, "is a posiitve number")
else:
    print(num, "is a negative number")