import random
# import FitnessCalc


class Chromosome:

    # constructor

    def __init__(self, db):
        self.db = db
        self.fitness = 0
        self.genes = []  # genes[day][time][course] 3D-list
        for _ in range(self.db.get_days()):
            row = [] # empty day
            for _ in range(self.db.get_times()):
                row.append([]) # empty slots
            self.genes.append(row)

    # For call to str(). Prints readable form

    def __str__(self):
        res = 'Chromosome Class:\n' + str(self.db)
        res += 'fitness = %i\n' % self.fitness
        res += 'genes:\n' + str(self.genes)
        return res

    # setters

    def set_gene(self, day, time, course, value):
        self.genes[day][time][course] = value
        self.fitness = 0

    # getters

    def get_gene(self, day, time, course):
        return self.genes[day][time][course]

    # public methods

    def get_fitness(self):
        # if self.fitness == 0:
        #     self.fitness = FitnessCalc.get_fitness(self)
        # return self.fitness
        return 1000
