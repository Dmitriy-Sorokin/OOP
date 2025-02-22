class Singleton:
    instance = None
    instance_base = None
    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.instance_base is None:
                cls.instance_base = object.__new__(cls)
            return cls.instance_base
        
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

class Game(Singleton):
    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name


# a = list(map(str.strip, sys.stdin.readlines()))
game = Game("Game")
game2 = Game("Game2")
print(game.name)
print(game2.name)