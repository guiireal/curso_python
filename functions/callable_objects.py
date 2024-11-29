class Power:
    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, value):
        return value**self.exponent


if __name__ == "__main__":
    square = Power(2)
    cube = Power(3)

    if callable(square) and callable(cube):
        print(square(2))
        print(cube(2))
