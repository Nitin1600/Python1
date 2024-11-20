# print(int())
# inf=iter(int,1)
# print(next(inf))
# print(next(inf))

class InfIter:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        num=self.num
        self.num+=2
        return num
a=iter(InfIter())
print(next(a))
print(next(a))
print(next(a))