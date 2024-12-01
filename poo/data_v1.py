class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def to_str(self):
        return f"{self.day}/{self.month}/{self.year}"


d1 = Data(12, 12, 2019)

print(d1.to_str())
