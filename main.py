class Neuron:
    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.exist = None

    def forward(self, x):
        self.x = x
        self.exist = x
        res = sum(map(lambda a, b: a*b, x, self.w))
        return self.f(res)

    def backlog(self):
        return self.exist

def sqrt(num):
    return num ** 2

zzz = Neuron([1, 2, 3], sqrt)
print(zzz.backlog())
print(zzz.forward([4, 5, 6]))  # Тут распечатается 1024, вот решение sum([1 * 4, 2 * 5, 3 * 6]) ** 2
print(zzz.backlog())