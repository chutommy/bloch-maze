class Coor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def valid(self):
        return self.x >= 0 and self.y >= 0
