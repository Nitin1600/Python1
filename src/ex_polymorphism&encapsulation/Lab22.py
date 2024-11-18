class Stationary:
    def _pen(self):
        self.d="Hyper"
        return self.d
    def __abcd(self):
        self.e="z"
        return self.e
class Main(Stationary):
    def __pencil(self):
        self.f="clan"
        return self.f
    def eraser(self):
        self.g="game"
        return self.g
obj=Main()
print(obj._pen())
# print(obj.__abcd())
print(obj._Main__pencil())
print(obj.eraser())
print(obj._Stationary__abcd())