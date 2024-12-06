from collections import deque
# list = ["a", "b", "c"]
# deq = deque(list)
# print(deq)
# deq.append("d")
# deq.appendleft("e")
# print(deq)
#
# deq.pop()
# deq.popleft()
# print(deq)

# list = ["Nitin"]
# deq = deque(list)
# print(deq)
# # print(deq.clear())
# print(deq.count("N"))

from collections import ChainMap
# dict1 = {"a":1, "b":2}
# dict2 = {"c":3, "d":4}
# chain_map = ChainMap(dict1, dict2)
# print(chain_map.maps)
# print(chain_map["a"])
# dict2["c"] = 5
# print(chain_map.maps)
# print(list(chain_map.keys()))
# print(list(chain_map.values()))
# dict3 = {"e":6, "f":7}
# new_chain_map = chain_map.new_child(dict3)
# print(new_chain_map)

from collections import namedtuple
Student = namedtuple("Student", "fname,lname,age")
s1 = Student("Jhon", "Clarke", "13")
print(s1.age)
s2 = Student._make(["Adam", "Joe", "18"])
print(s2)
s2 = s1._asdict()
print(s2)

s2 = s1._replace(age=14)
print(s1)
print(s2)