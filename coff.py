
class Coff:
    def __init__(self, coff_hole = 0, coff_rem = 0, coff_deep = 0, coff_avg_height = 0, coff_diff = 0):
        self.coff_hole = coff_hole
        self.coff_rem = coff_rem
        self.coff_deep = coff_deep
        self.coff_avg_height = coff_avg_height
        self.coff_diff = coff_diff
        self.fitness = 0

    def __str__(self):
        l = [self.coff_hole, self.coff_rem, self.coff_deep, self.coff_avg_height, self.coff_diff]
        return ', '.join([str(x) for x in l])

    def calculate_fitness(self, game):
        self.fitness = game.playWithoutLookingAhead(self)