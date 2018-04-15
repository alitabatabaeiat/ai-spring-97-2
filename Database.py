from Course import Course

class Database:

    # constructor
    def __init__(self):
        self.days = 0
        self.times = 0
        self.courses = []
        self.happiness = []
        self.professors = []
        self.sadness = []
        self.population = 0

    # For call to str(). Prints readable form

    def __str__(self):
        res = 'Database Class:\n'
        res += 'days = %i\n' % self.days
        res += 'times = %i\n' % self.times
        res += self.str_courses()
        res += self.str_happiness()
        res += self.str_professors()
        res += self.str_sadness()
        res += 'population = %i\n' % self.population
        return res

    # str

    def str_courses(self):
        res = 'courses:\n'
        for i in range(self.get_courses_size()):
            res += ('%i: ' % (i + 1)) + str(self.get_course(i)) # consider course ids starts from 1

        return res

    def str_happiness(self):
        return 'happiness:\n' + ' '.join(str(i) for i in self.happiness) + '\n'

    def str_professors(self):
        res = 'professors:\n'
        for p in self.professors:
            res += ' '.join(str(i) for i in p) + '\n'

        return res

    def str_sadness(self):
        res = 'sadness:\n'
        for s in self.sadness:
            res += ' '.join(str(i) for i in s) + '\n'

        return res

    # setters

    def set_days(self, days):
        self.days = days

    def set_times(self, times):
        self.times = times

    def set_courses(self, courses_size):
        for _ in range(courses_size):
            self.courses.append(Course())

    def add_professor_to_course(self, index, professor):
        self.courses[index].add_professor(professor)

    def set_happiness(self, happiness):
        self.happiness = happiness

    def set_professors(self, professors):
        self.professors = professors

    def set_sadness(self, sadness):
        self.sadness = sadness

    def set_population(self, population):
        self.population = population

    # getters

    def get_days(self):
        return self.days

    def get_times(self):
        return self.times

    def get_courses(self):
        return self.courses

    def get_course(self, index):
        return self.courses[index]

    def get_courses_size(self):
        return len(self.courses)

    def get_happiness(self):
        return self.happiness

    def get_professors_number(self):
        return len(self.professors)

    def get_professors(self):
        return self.professors

    def get_sadness(self):
        return self.sadness

    def get_population(self):
        return self.population