class entity():
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.level = 1
        self.symbol = symbol

    def render(window):
        window.addch(self.x, self.y, self.symbol)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
