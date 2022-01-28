"""Создайте итератор (обьект класса), который будет возвращать числа фибоначчи."""


class FibonachiNumbers:

    def __init__(self, limit):
        if not isinstance(limit, int):
            raise Exception
        self.limit = limit

    def __iter__(self):
        self.fib1, self.fib2 = 1, 1

        return self

    def __next__(self):
        self.fib = self.fib1
        if self.fib > self.limit:
            raise StopIteration
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return self.fib


iterator = FibonachiNumbers(100)
for i in iterator:
    print(i, end=' ')


"""Создайте генератор (функцию), который будет возвращать числа фибоначчи."""


def fib_generator(val_fib):
    if not isinstance(val_fib, int):
        raise Exception('Only int')
    fib1, fib2 = 1, 1
    while val_fib > 0:
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1
        val_fib -= 1


fib = fib_generator(30)
for i in fib:
    print(i)
