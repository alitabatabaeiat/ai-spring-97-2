import copy
import operator
import random

# constants
import time

POPULATION_SIZE = 30
REPEATS = 5
CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 5
NUM_OF_ELITE_SCHEDULES = 3

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


def add_new_classes(schedule):
    schedule[1] = copy.deepcopy(courses)
    for i in range(len(schedule[0])):
        for j in range(len(schedule[1])):
            if schedule[0][i][0] == schedule[1][j][0]:
                del schedule[1][j]
                break
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


def remove_conflicts(schedule):
    i = 0
    while i < len(schedule[0]):
        flag = False
        for j in range(len(schedule[0])):
            if i == j:
                continue
            if schedule[0][i][0] == schedule[0][j][0]:
                del schedule[0][random.randint(0, 1)]
                flag = True
                break
            if is_equal_slot(schedule[0][i][2], schedule[0][j][2]) \
                    and schedule[0][i][3] == schedule[0][j][3]:
                del schedule[0][random.randint(0, 1)]
                flag = True
                break
        if not flag:
            i += 1
    return schedule


def select_tournament_population(p):
    tournament_population = []
    for i in range(TOURNAMENT_SIZE):
        tournament_population.append(p[random.randint(0, len(p) - 1)])
    return tournament_population


def crossover_schedule(schedule1, schedule2):
    new_schedule = [[], [], 0, True]
    min_size = len(schedule1[0])
    max_size = len(schedule1[0])
    if max_size < len(schedule2[0]):
        max_size = len(schedule2[0])
    else:
        min_size = len(schedule2[0])
    for i in range(max_size):
        if (random.uniform(0, 1) < 0.5 and i < min_size) or (min_size <= i < len(schedule1[0])):
            new_schedule[0].append(schedule1[0][i])
        else:
            new_schedule[0].append(schedule2[0][i])
    return remove_conflicts(new_schedule)


def crossover_population(p):
    new_population = []
    for i in range(0, NUM_OF_ELITE_SCHEDULES):
        new_population.append(p[i])
    for i in range(NUM_OF_ELITE_SCHEDULES, POPULATION_SIZE):
        if random.uniform(0, 1) < CROSSOVER_RATE:
            schedule1 = sort(select_tournament_population(p))[0]
            schedule2 = sort(select_tournament_population(p))[0]
            new_population.append(add_new_classes(crossover_schedule(schedule1, schedule2)))
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
    # [classes, courses, fitness, is_fitness_changed] -> list of properties needed for each class
    schedule = [[], copy.deepcopy(courses), 0, True]
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
    calculate_fitness(schedule)  # calculate fitness of this schedule
    return schedule


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
    print(str_schedule(schedule))
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
    read_inputs()
    population = generate_population()
    sort(population)
    generation = 1
    counter = 0
    max_fitness = population[0][2]
    while time.time() - start < 120 and counter < 2000:
        population = evolve(population)
        for schedule in population:
            calculate_fitness(schedule)
        sort(population)
        fitness = population[0][2]
        if fitness - max_fitness < 50:
            counter += 1
        else:
            print(counter)
            counter = 0
        if fitness > max_fitness:
            max_fitness = fitness
        # print(fitness)
        generation += 1
    print(generation)
    print_final_output(population[0])
