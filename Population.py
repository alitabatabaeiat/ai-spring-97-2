from Chromosome import Chromosome


class Population:

    # constructor

    def __init__(self, db):
        self.db = db
        self.chromosomes = []

    # For call to str(). Prints readable form

    def __str__(self):
        res = '-----------------------\n'
        res += 'Population Class:\n' + self.str_chromosomes()
        res += '-----------------------'
        return res

    # str

    def str_chromosomes(self):
        res = 'chromosomes:\n'
        for chromosome in self.get_chromosomes():
            res += str(chromosome)
        return res

    # setters

    def set_chromosome(self, index, chromosome):
        self.chromosomes[index] = chromosome
        return self

    # getters

    def get_population(self):
        return self.db.get_population()

    def get_chromosome(self, index):
        return self.chromosomes[index]

    def get_chromosomes(self):
        return self.chromosomes

    def get_fittest(self):
        fittest = self.get_chromosome(0)

        for i in self.chromosomes:
            if fittest.get_fitness() < i.get_fitness():
                fittest = self.get_chromosome(i)

        return fittest

    # public methods

    def generate(self):
        for i in range(self.get_population()):
            self.chromosomes.append(Chromosome(self.db))