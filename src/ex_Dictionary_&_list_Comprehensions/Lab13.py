# a = []
# for letter in "human":
#     a.append(letter)
# print(a)

# a = [letter for letter in "human"]
# print(a)

# a = list(map(lambda x:x, "human"))
# print(a)

# a = [x for x in range(20) if x % 2 == 0]
# print(a)

# a = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
# print(a)

# a = ["Even" if i%2 == 0 else "Odd" for i in range(20)]
# print(a)

# transposed = []
# matrix = [[1,2,3,4],[4,5,6,8]]
#
# for i in range(len(matrix[0])):
#     transposed_row= []
#
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
#
# print(transposed)

matrix = [[1,2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)