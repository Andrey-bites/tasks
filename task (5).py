import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)


class Calculator:
    a = 123
    b = 234

    def __init__(self, a_new, b_new):
        if isinstance(a_new, int):
            self.a = a_new
        if isinstance(b_new, int):
            self.b = b_new

    def decorator_logging(func):

        def wrapper(*args):
            logging.info(f'The input values A and B are {args}')
            res = func(*args)
            return res
        return wrapper


    @decorator_logging
    def sum(self):
        return self.a + self.b

    @decorator_logging
    def multiply(self):
        return self.a * self.b

    @decorator_logging
    def divide(self):
        return self.a / self.b

    @decorator_logging
    def subtract(self):
        return self.a - self.b

    @decorator_logging    
    def dec_logging():
        pass


s = Calculator(2, 5)

ne = s.sum()
print(ne)
