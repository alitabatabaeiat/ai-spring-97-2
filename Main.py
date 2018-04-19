import copy
import operator
import random
import time

# constants

POPULATION_SIZE = 100
REPEATS = 5
CROSSOVER_RATE = 0.7
TOURNAMENT_SIZE = int(25 * POPULATION_SIZE / 100)
NUM_OF_ELITE_SCHEDULES = int(POPULATION_SIZE / 10)
GENERATION_WITH_LITTLE_DIFFERENCE = 700
FITNESS_DIFFERENCE = 30

# Global vars
slots = []  # (day, time) -> list of slot tuples
courses = []  # [id, happiness, professors, sadness] -> list of course lists
answer = []


def read_inputs():
    days, times = map(int, input().split())
    for day in range(days):
        row = []
        for time in range(times):
            row.append([])
            slots.append((day, time))
        answer.append(row)

    course_number = int(input())
    happiness = list(map(int, input().split()))

    for i in range(course_number):
        courses.append([i + 1, happiness[i], [], ()])

    p = int(input())
    for i in range(p):
        professor = list(map(int, input().split()))
        del professor[0]
        for j in professor:
            courses[j - 1][2].append(i)
            # j is course id (**consider course ids starts from 1**)
            # i is professor id in the list of professors

    for i in range(len(courses)):
        sadness = tuple(map(int, input().split()))
        courses[i][3] = sadness

    i = 0
    while i < len(courses):
        if len(courses[i][2]) == 0:
            del courses[i]
        else:
            i += 1


def has_conflict(schedule, class1):
    for class2 in schedule[0]:
        if class1[0] == class2[0] or (is_equal_slot(class1[2], class2[2]) and class1[3] == class2[3]):
            return True
    return False


def add_new_classes(schedule):
    while len(schedule[1]) > 0:
        course = schedule[1][random.randint(0, len(schedule[1]) - 1)]
        for _ in range(REPEATS):
            # (id, course, slot, professor) -> tuple for a class
            new_class = (course[0], course, slots[random.randint(0, len(slots) - 1)])  # professor not added to it yet
            professors = get_professors_without_conflict_on_slot(schedule, course, new_class[2])
            if len(professors) > 0:
                new_class += (professors[random.randint(0, len(professors) - 1)],)  # professor added
                schedule[0].append(new_class)  # add new class to schedule list
                break
        schedule[1].remove(course)  # remove this course from courses of this schedule
    return schedule


def select_tournament_population(p):
    tournament_population = []
    for i in range(TOURNAMENT_SIZE):
        tournament_population.append(p[random.randint(0, len(p) - 1)])
    return tournament_population


def crossover_schedule(schedule1, schedule2):
    new_schedule = [[], copy.deepcopy(courses), 0]
    classes = copy.deepcopy(schedule1[0]) + copy.deepcopy(schedule2[0])
    i = 0
    while i < len(classes):
        random_class = classes[random.randint(0, len(classes) - 1)]
        if not has_conflict(new_schedule, random_class):
            new_schedule[0].append(random_class)
            new_schedule[1].remove(random_class[1])
        classes.remove(random_class)
    return new_schedule


def crossover_population(p):
    new_population = []
    for i in range(0, NUM_OF_ELITE_SCHEDULES):
        new_population.append(p[i])
    for i in range(NUM_OF_ELITE_SCHEDULES, POPULATION_SIZE):
        if random.uniform(0, 1) < CROSSOVER_RATE:
            schedule1 = sort(select_tournament_population(p))[0]
            schedule2 = sort(select_tournament_population(p))[0]
            new_population.append(calculate_fitness(add_new_classes(crossover_schedule(schedule1, schedule2))))
        else:
            new_population.append(p[i])
    return new_population


def evolve(p):
    return crossover_population(p)


def is_equal_slot(slot1, slot2):
    return slot1[0] == slot2[0] and slot1[1] == slot2[1]


def get_professors_without_conflict_on_slot(schedule, course, slot):
    # course can not be duplicate because after choosing a course, it will be delete
    professors = list(course[2])
    for _class in schedule[0]:
        if is_equal_slot(_class[2], slot):
            # remove each professor of the new course that is duplicate
            professors = [x for x in professors if x != _class[3]]
    return professors


def generate_schedule():
    # [classes, courses, fitness] -> list of properties needed for each class
    schedule = [[], copy.deepcopy(courses), 0]
    while len(schedule[1]) > 0:
        course = schedule[1][random.randint(0, len(schedule[1]) - 1)]
        for _ in range(REPEATS):
            # (id, course, slot, professor) -> tuple for a class
            new_class = (course[0], course, slots[random.randint(0, len(slots) - 1)])  # professor not added to it yet
            professors = get_professors_without_conflict_on_slot(schedule, course, new_class[2])
            if len(professors) > 0:
                new_class += (professors[random.randint(0, len(professors) - 1)],)  # professor added
                schedule[0].append(new_class)  # add new class to schedule list
                break
        schedule[1].remove(course)  # remove this course from courses of this schedule
    return calculate_fitness(schedule)  # calculate fitness of this schedule


def generate_population():
    new_population = []  # list of schedules
    for i in range(POPULATION_SIZE):
        schedule = generate_schedule()
        new_population.append(schedule)
    return new_population


def calculate_fitness(schedule):
    fitness = 0
    classes = schedule[0]
    for i in range(len(classes)):
        # multiply 2 -> because sadness will calc two times
        c1 = classes[i]
        fitness += 2 * c1[1][1]
        for j in range(len(classes)):
            if i == j:
                continue
            c2 = classes[j]
            if is_equal_slot(c1[2], c2[2]):
                fitness -= c1[1][3][c2[0] - 1]  # *** sadness will calc two times ***
    schedule[2] = fitness / 2  # fitness was multiplied
    return schedule


def sort(p):
    p.sort(key=operator.itemgetter(2), reverse=True)
    return p


def str_population(p):
    res = 'schedules:\n'
    for schedule in p:
        res += str_schedule(schedule)
    return res


def str_schedule(schedule):
    res = '-----------------------\n'
    res += 'Schedule:\n'
    res += '\tfitness = %f\n' % schedule[2]
    res += '\tclasses: \n%s\n' % str_classes(schedule[0])
    res += '-----------------------'
    return res


def str_classes(classes):
    res = ''
    for c in classes:
        res += '\t\t%s' % str_class(c)
    return res


def str_class(c):
    slot = c[2]
    return 'Class %i:\tday = %i \ttime = %i \tprofessor = %i\n' % \
           (c[0], slot[0], slot[1], c[3])


def fill_answer(schedule):
    for c in schedule[0]:
        answer[c[2][0]][c[2][1]].append((c[0], c[3]))


def print_final_output(schedule):
    file = open('out.txt', 'w')
    file.write('%i\n' % schedule[2])
    fill_answer(schedule)
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer[i][j].sort(key=operator.itemgetter(0))
            for k in range(len(answer[i][j])):
                file.write('%i %i %i %i\n' % (i, j, answer[i][j][k][0], answer[i][j][k][1]))
    file.close()


if __name__ == '__main__':
    start = time.time()
    print('population size = %i\nrepeats = %i\ncrossover rate = %i\ntournament size = %i\nnumber of elite schedules = '
          '%i\ngenerations with little diffrence = %i\nfitness diffrence = '
          '%i\n--------------------------------------------------------' % (POPULATION_SIZE, REPEATS, CROSSOVER_RATE,
                                                                            TOURNAMENT_SIZE, NUM_OF_ELITE_SCHEDULES,
                                                                            GENERATION_WITH_LITTLE_DIFFERENCE,
                                                                            FITNESS_DIFFERENCE))
    read_inputs()
    population = generate_population()
    sort(population)
    generation = 1
    counter = 0
    max_fitness = population[0][2]
    print('fitness of fittest schedule of initial population: %i' % max_fitness)
    while time.time() - start < 120:
        population = evolve(population)
        sort(population)
        fitness = population[0][2]
        if fitness - max_fitness < FITNESS_DIFFERENCE:
            counter += 1
        else:
            counter = 0
        if fitness > max_fitness:
            max_fitness = fitness
        generation += 1
    print('max_fitness after %isec and %i generation: %i' % (time.time() - start, generation, max_fitness))
    print_final_output(population[0])
