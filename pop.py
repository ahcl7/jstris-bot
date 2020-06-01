class Population():
    def __init__(self, size = 0):
        self.size = size
        self.pop = [0] * size

    def set(self, idx, coff):
        self.pop[idx] = coff
    
    def calculate_fitness(self, Game):
        for coff in self.pop:
            coff.calculate_fitness(Game())

    def get_total_fitness(self):
        res = 0
        for coff in self.pop:
            res += coff.fitness
        return res

    def get_best_fitness_idx(self):
        best = -1
        res = -1
        for i in range(len(self.pop)):
            if (self.pop[i].fitness > best):
                best = self.pop[i].fitness
                res = i
            print(i, self.pop[i].fitness)
        return res