class Animel:

    def __init__(self, color, legs):  # init constructor
        self.color = color
        self.legs = legs

    def eats(self):
        print("I eats dear")


tigers = Animel('yellow', 4)
print("I am tiger, My color is {}, I have {} legs."
      .format(tigers.color, tigers.legs))
tigers.eats()


class Monstar(Animel):
    def attack(self):
        print("huhu")


tigers = Monstar('Black', 4)
print("I am tiger, My color is {}, I have {} legs."
      .format(tigers.color, tigers.legs))
tigers.eats()
tigers.attack()
