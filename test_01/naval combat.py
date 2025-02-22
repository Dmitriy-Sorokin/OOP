import random


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def is_collide(self, ship):
        x1, y1 = self._x, self._y
        x2, y2 = ship.get_start_coords()

        for i in range(self._length):
            for j in range(ship._length):
                if (self._tp == 1 and x1 + i == x2 + j and y1 == y2) or \
                        (self._tp == 2 and x1 == x2 and y1 + i == y2 + j):
                    return True
                if abs((x1 + (i if self._tp == 1 else 0)) - (x2 + (j if ship._tp == 1 else 0))) <= 1 and \
                        abs((y1 + (i if self._tp == 2 else 0)) - (y2 + (j if ship._tp == 2 else 0))) <= 1:
                    return True
        return False

    def is_out_pole(self, size):
        x, y = self._x, self._y
        if self._tp == 1:
            return not (0 <= x <= size - self._length and 0 <= y < size)
        else:
            return not (0 <= x < size and 0 <= y <= size - self._length)

    def __getitem__(self, index):
        return self._cells[index]

    def __setitem__(self, index, value):
        self._cells[index] = value
        if value == 2:
            self._is_move = False


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        ships = [Ship(4, tp=random.randint(1, 2))]
        ships += [Ship(3, tp=random.randint(1, 2)) for _ in range(2)]
        ships += [Ship(2, tp=random.randint(1, 2)) for _ in range(3)]
        ships += [Ship(1, tp=random.randint(1, 2)) for _ in range(4)]

        for ship in ships:
            while True:
                x, y = random.randint(0, self._size - 1), random.randint(0, self._size - 1)
                ship.set_start_coords(x, y)
                if not ship.is_out_pole(self._size) and \
                        not any(s.is_collide(ship) for s in self._ships):
                    self._ships.append(ship)
                    break

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            go = random.choice([-1, 1])
            if ship._is_move:
                ship.move(go)
                if ship.is_out_pole(self._size) or any(s.is_collide(ship) for s in self._ships if s != ship):
                    ship.move(-go)

    def show(self):
        pole = [[0] * self._size for _ in range(self._size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            for i in range(ship._length):
                if ship._tp == 1:
                    pole[y][x + i] = ship[i]
                else:
                    pole[y + i][x] = ship[i]

        for row in pole:
            print(" ".join(map(str, row)))

    def get_pole(self):
        return tuple(tuple(row) for row in [[0] * self._size for _ in range(self._size)])


# Пример использования:
SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

print("\nПосле движения кораблей:\n")
pole.move_ships()
pole.show()
