from Population import Population
from Schedule import Schedule
import random


class GeneticAlgorithm:

    # constructor

    def __init__(self, db):
        self.db = db
        self.CROSSOVER_RATE = 0.9
        self.MUTATION_RATE = 0.1
        self.TOURNAMENT_SIZE = 3
        self.NUM_OF_ELITE_SCHEDULES = 1

    # getters

    def get_db(self):
        return self.db

    # public methods

    def evolve(self, population):
        return self.mutate_population(self.crossover_population(population))

    def crossover_population(self, population):
        crossover_population = Population(self.get_db())
        crossover_population.generate_empty(self.get_db().get_population())
        for i in range(0, self.NUM_OF_ELITE_SCHEDULES):
            crossover_population.set_schedule(i, population.get_schedule(i))
        for i in range(self.NUM_OF_ELITE_SCHEDULES, population.schedules_size()):
            if random.uniform(0, 1) < self.CROSSOVER_RATE:
                schedule1 = self.select_tournament_population(population).sort().get_schedule(0)
                schedule2 = self.select_tournament_population(population).sort().get_schedule(0)
                crossover_population.set_schedule(i, self.crossover_schedule(schedule1, schedule2))
            else:
                crossover_population.set_schedule(i, population.get_schedule(i))
        return crossover_population

    def crossover_schedule(self, schedule1, schedule2):
        crossover_schedule = Schedule(self.get_db())
        min_size = schedule1.classes_size()
        if min_size > schedule2.classes_size():
            min_size = schedule2.classes_size()
        crossover_schedule.initialize_empty(min_size)
        for i in range(min_size):
            if random.uniform(0, 1) < 0.5:
                crossover_schedule.set_class(i, schedule1.get_class(i))
            else:
                crossover_schedule.set_class(i, schedule2.get_class(i))
        return crossover_schedule.remove_conflicts()

    def mutate_population(self, population):
        mutate_population = Population(self.get_db())
        mutate_population.generate_empty(self.get_db().get_population())
        for i in range(0, self.NUM_OF_ELITE_SCHEDULES):
            mutate_population.set_schedule(i, population.get_schedule(i))
        for i in range(self.NUM_OF_ELITE_SCHEDULES, population.schedules_size()):
                mutate_population.set_schedule(i, self.mutate_schedule(population.get_schedule(i)))
        return mutate_population

    def mutate_schedule(self, mutate_schedule):
        schedule = Schedule(self.get_db()).initialize()
        min_size = schedule.classes_size()
        if min_size > mutate_schedule.classes_size():
            min_size = mutate_schedule.classes_size()
        for i in range(min_size):
            if random.uniform(0, 1) < self.MUTATION_RATE:
                mutate_schedule.set_class(i, schedule.get_class(i))
        return mutate_schedule.remove_conflicts()

    def select_tournament_population(self, population):
        tournament_population = Population(self.get_db())
        tournament_population.generate_empty(self.TOURNAMENT_SIZE)
        for i in range(self.TOURNAMENT_SIZE):
            tournament_population.set_schedule(i, population.get_schedule(random.randint(0, population.schedules_size() - 1)))
        return tournament_population
