from collections import Counter, defaultdict
# cnt = Counter()
# list = [1,2,3,4,5,6,7,5,3,]
# Counter(list)
# Counter({1:3,2:4})

# list = [1,2,3,4,5,6,4,3]
# cnt = Counter(list)
# print(cnt[1])

# cnt = Counter({1:3,2:4})
# print(list(cnt.elements()))

# list = [1,2,3,4,5,3,1,3,4,5,5,5,5,6,7,8,8]
# cnt = Counter(list)
# print(cnt.most_common())

# cnt = Counter({1:4,2:5})
# deduct = ({1:2, 2:1})
# cnt.subtract(deduct)
# print(cnt)

from collections import Counter
# nums = defaultdict(int)
# nums['one'] = 1
# nums['two'] = 2
# print(nums['three'])

from collections import defaultdict
# count = defaultdict(int)
# names_list = ["Mike","Jhon","Mike","Anna","Mike","Jhon","Jhon","Mike","Mike","Britney","Smith","Anna","Smith"]
# for names in names_list:
#     count[names] += 1
# print(count)

# from collections import defaultdict
# count = defaultdict(int)
# words_list = ["N","i","t","i","n"]
# for letters in words_list:
#     count[letters] += 1
# print(count)

from collections import OrderedDict
# od = OrderedDict()
# od["a:"]=1
# od["b:"]=2
# od["c:"]=3
# print(od)
# for key, value in od.items():
#     print(key, value)

list=["a","c","c","a","c","b","a","a","b"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)

