import operator
import time

from Database import Database
from GeneticAlgorithm import GeneticAlgorithm
from Population import Population

class Main:

    # constants
    #
    POPULATION_SIZE = 30
    REPEATS = 5
    CROSSOVER_RATE = 0.9
    MUTATION_RATE = 0.1
    TOURNAMENT_SIZE = 5
    NUM_OF_ELITE_SCHEDULES = 3

    database = None
    days = 0
    times = 0

    @staticmethod
    def read_inputs():
        Main.database = Database()

        Main.days, Main.times = map(int, input().split())
        c = int(input())
        happiness = list(map(int, input().split()))
        Main.database.set_slots(Main.days, Main.times) \
            .set_courses(c, happiness)

        p = int(input())
        for i in range(p):
            professor = list(map(int, input().split()))
            del professor[0]
            for j in professor:
                Main.database.add_professor_to_course(j - 1, i)
                # j is course id (**consider course ids starts from 1**)
                # i is professor id in the list of professors

        for i in range(c):
            sadness = list(map(int, input().split()))
            Main.database.get_course(i).set_sadness(sadness)

        Main.database.remove_courses_without_professor()

    @staticmethod
    def get_normalized_answer(schedule):
        answer = []
        for i in range(Main.days):
            row = []
            for j in range(Main.times):
                row.append([])
            answer.append(row)
        for _class in schedule.get_classes():
            answer[_class.get_slot().get_day()][_class.get_slot().get_time()].append((_class.get_id(), _class.get_professor()))
        return answer

    @staticmethod
    def print_best_schedule(schedule):
        file = open('out.txt', 'w')
        file.write('%i\n' % schedule.get_fitness())
        answer = Main.get_normalized_answer(schedule)
        for i in range(len(answer)):
            for j in range(len(answer[i])):
                answer[i][j].sort(key=operator.itemgetter(0))
                for k in range(len(answer[i][j])):
                    file.write('%i %i %i %i\n' % (i, j, answer[i][j][k][0], answer[i][j][k][1]))
        file.close()

    @staticmethod
    def find_solution(start):
        ga = GeneticAlgorithm(Main.database)
        population = Population(Main.database).generate()
        max_fitness = population.get_fittest().get_fitness()
        counter, generation = 0, 1
        while time.time() - start < 120 and counter < 1200:
            population = ga.evolve(population)
            fitness = population.get_fittest().get_fitness()
            if fitness - max_fitness < 50:
                counter += 1
            else:
                counter = 0
            if fitness > max_fitness:
                max_fitness = fitness
            generation += 1
        Main.print_best_schedule(population.get_fittest())

    @staticmethod
    def main():
        start = time.time()
        Main.read_inputs()
        # print(Main.database.courses_size())

        Main.database.set_population(Main.POPULATION_SIZE) \
            .set_repeats(Main.REPEATS)
        Main.find_solution(start)


if __name__ == '__main__':
    Main.main()
