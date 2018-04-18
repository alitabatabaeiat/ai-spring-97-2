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
        return self.crossover_population(population)

    def crossover_population(self, population):
        crossover_population = Population(self.get_db())
        # crossover_population.generate_empty(self.get_db().get_population())
        for i in range(0, self.NUM_OF_ELITE_SCHEDULES):
            crossover_population.add_schedule(population.get_schedule(i))
        for i in range(self.NUM_OF_ELITE_SCHEDULES, population.schedules_size()):
            if random.uniform(0, 1) < self.CROSSOVER_RATE:
                schedule1 = self.select_tournament_population(population).sort().get_schedule(0)
                schedule2 = self.select_tournament_population(population).sort().get_schedule(0)
                crossover_population.add_schedule(self.crossover_schedule(schedule1, schedule2))
            else:
                crossover_population.add_schedule(population.get_schedule(i))
        return crossover_population

    def crossover_schedule(self, schedule1, schedule2):
        crossover_schedule = Schedule(self.get_db())
        min_size = schedule1.classes_size()
        max_size = schedule1.classes_size()
        if max_size < schedule2.classes_size():
            max_size = schedule2.classes_size()
        else:
            min_size = schedule2.classes_size()
        for i in range(max_size):
            if (random.uniform(0, 1) < 0.5 and i < min_size) or (min_size <= i < schedule1.classes_size()):
                crossover_schedule.add_class(schedule1.get_class(i))
            else:
                crossover_schedule.add_class(schedule2.get_class(i))
        return crossover_schedule.remove_conflicts().remove_exists_courses().fill_schedule().calculate_fitness()

    def select_tournament_population(self, population):
        tournament_population = Population(self.get_db())
        for i in range(self.TOURNAMENT_SIZE):
            tournament_population.add_schedule(population.get_schedule(random.randint(0, population.schedules_size() - 1)))
        return tournament_population
