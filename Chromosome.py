import random
# import FitnessCalc


class Chromosome:
    length = 0
    num_of_courses = 0

    # constructor

    def __init__(self):
        self.fitness = 0
        self.genes = []
        for i in list(range(self.length)):
            self.genes.append(random.randint(1, self.num_of_courses))

    # For call to str(). Prints readable form

    def __str__(self):
        genes_string = ','.join(str(i) for i in self.genes)
        return 'gene_length = %i -- num_of_courses = %i -- chromosome = [%s]\n' % (self.length, self.num_of_courses, genes_string)

    # getters & setters

    def get_gene(self, index):
        return self.genes[index]

    def set_gene(self, index, value):
        self.genes[index] = value
        self.fitness = 0

    # public methods

    def get_fitness(self):
        if self.fitness == 0:
            # self.fitness = FitnessCalc.get_fitness(self)
            self.fitness = 1000
        return self.fitness

    # static methods

    @staticmethod
    def size():
        return Chromosome.length

    @staticmethod
    def set_gene_length(length):
        Chromosome.length = length

    @staticmethod
    def set_num_of_courses(num_of_chromosome):
        Chromosome.num_of_courses = num_of_chromosome
