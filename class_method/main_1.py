class Victor:
    MIN_COORD = 0
    MAX_COOED = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= cls.MAX_COOED

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y
