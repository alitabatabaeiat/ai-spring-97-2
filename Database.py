import random
from Course import Course
from Slot import Slot


class Database:

    # constructor
    def __init__(self):
        self.slots = []
        self.courses = []
        self.population = 0
        self.repeats = 0  # number of repeats try to put a specific course on a slot

    # For call to str(). Prints readable form

    def __str__(self):
        res = 'Database Class:\n'
        res += self.str_courses()
        res += 'population = %i\n' % self.population
        res += 'repeats = %i\n' % self.repeats
        return res

    # str

    def str_courses(self):
        res = 'courses:\n'
        for course in self.get_courses():
            res += str(course)
        return res

    # setters

    def set_slot(self, day, time):
        self.slots.append(Slot(day, time))
        return self

    def set_slots(self, days, times):
        for day in range(days):
            for time in range(times):
                self.set_slot(day, time)
        return self

    def set_courses(self, courses, happiness):
        for i in range(courses):
            self.courses.append(Course(i, happiness[i]))
        return self

    def set_population(self, population):
        self.population = population
        return self

    def set_repeats(self, repeats):
        self.repeats = repeats
        return self

    # getters

    def get_slot(self, index):
        return self.slots[index]

    def get_slots(self):
        return self.slots

    def get_random_slot(self):
        return self.slots[random.randint(0, self.slots_size() - 1)]

    def get_courses(self):
        return self.courses

    def get_course(self, index):
        return self.courses[index]

    def get_random_course(self):
        return self.courses[random.randint(0, self.courses_size() - 1)]

    def get_population(self):
        return self.population

    def get_repeats(self):
        return self.repeats

    # public methods

    def slots_size(self):
        return len(self.slots)

    def courses_size(self):
        return len(self.courses)

    def add_professor_to_course(self, index, professor):
        self.courses[index].add_professor(professor)
