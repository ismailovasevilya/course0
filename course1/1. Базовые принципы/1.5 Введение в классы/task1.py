class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        if v < self.capacity - self.count :
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.count += v