# square_dict = dict()
# for num in range(1,11):
#     square_dict[num] = num*num
# print(square_dict)

# square_dict = {num:num*num for num in range(1,11)}
# print(square_dict)

# old_price = {"coffee":1, "bread":4, "milk":5}
# dollar_to_pound = 0.76
# new_price = {item:value*dollar_to_pound for (item,value) in old_price.items()}
# print(new_price)

# original_dict = {"michael":38, "Jhon":28, "Orton":57, "Mandy":65}
# even_dict = {k:v for (k,v) in original_dict.items() if v % 2 == 0}
# print(even_dict)

# original_dict = {"michael":38, "Jhon":28, "Orton":33, "Mandy":23}
# even_dict = {k:v for (k,v) in original_dict.items() if v % 2 != 0 if v < 40}
# print(even_dict)

# original_dict = {"michael":38, "Jhon":28, "Orton":41, "Mandy":23}
# new_dict1 = {k:("old" if v > 40 else "young") for (k,v) in original_dict.items()}
# print(new_dict1)

# dictionary = {
#     k1:{k2:k1*k2 for k2 in range(1,6)} for k1 in range (2,5)
# }
# print(dictionary)

# dictionary = dict()
# for k1 in range(2,5):
#     dictionary[k1] = {k2:k1*k2 for k2 in range(1,6)}
# print(dictionary)

dictionary = dict()
for k1 in range(2,5):
    dictionary[k1] = dict()
    for k2 in range(1,6):
        dictionary[k1][k2] = k1*k2
print(dictionary)