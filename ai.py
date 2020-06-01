from player import *
from piece import *
from game import *
from coff import *
from pop import *
from bisect import bisect_left
import random
import time

if __name__ == '__main__':
    def train():
        base = Coff(17.72, -2, 5, 1, 1)

        pop = Population(50)
        for i in range(pop.size - 1):
            A = base.coff_hole + random.random() * 10 - 5
            
            B = base.coff_rem + random.random() * 10 - 5
            
            C = base.coff_deep + random.random() * 10 - 5
            
            D = base.coff_avg_height + random.random() * 10 - 5
            
            E = base.coff_diff + random.random() * 10 - 5

            pop.set(i, Coff(A, B, C, D, E))
        pop.set(pop.size - 1, base)
        
        def calculate_fitness():
            pop.calculate_fitness(Game)

        def selection():
            
            total_fitness = pop.get_total_fitness()
            propabilities = [0]
            for coff in pop.pop:
                propabilities.append(propabilities[-1] + coff.fitness / total_fitness)
            
            def rand():
                x = random.random()
                idx = bisect_left(propabilities, x) - 1
                return pop.pop[idx]
            
            def cross_over(coff1, coff2):
                x = random.random()
                A = (coff1.coff_hole * x + coff2.coff_hole * (1 - x))
                x = random.random()
                
                B = (coff1.coff_rem * x + coff2.coff_rem * (1 - x))
                x = random.random()
                
                C = (coff1.coff_deep * x + coff2.coff_deep * (1 - x))
                x = random.random()
                
                D = (coff1.coff_avg_height * x+ coff2.coff_avg_height * (1 - x))
                x = random.random()
                
                E = (coff1.coff_diff * x+ coff2.coff_diff * (1 - x))
                return Coff(A, B, C, D, E)
        
            def mutate(coff):
                a = [coff.coff_hole, coff.coff_rem, coff.coff_deep, coff.coff_avg_height, coff.coff_diff]
                for i in range(len(a)):
                    if (random.random() < 0.1):
                        a[i] = a[i] + random.random() * 0.2 - 0.1
                return Coff(a[0], a[1], a[2], a[3], a[4])

            new_pop = Population(pop.size)
            for i in range(pop.size):
                a = rand()
                b = rand()
                c = cross_over(a, b)
                c = mutate(c)
                new_pop.pop[i] = c
            pop.pop = new_pop.pop

        while (True):
            calculate_fitness()
            idx = pop.get_best_fitness_idx()
            print(pop.pop[idx].fitness)
            print(pop.pop[idx])
            selection()


    train()
