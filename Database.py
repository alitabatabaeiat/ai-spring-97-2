from Course import Course


class Database:

    # constructor
    def __init__(self):
        self.days = 0
        self.times = 0
        self.courses = []
        self.professors = []
        self.population = 0
        self.repeat = 0  # number of repeats try to put a specific course on a slot

    # For call to str(). Prints readable form

    def __str__(self):
        res = 'Database Class:\n'
        res += 'days = %i\n' % self.days
        res += 'times = %i\n' % self.times
        res += self.str_courses()
        res += self.str_professors()
        res += 'population = %i\n' % self.population
        res += 'repeat = %i\n' % self.repeat
        return res

    # str

    def str_courses(self):
        res = 'courses:\n'
        for course in self.get_courses():
            res += str(course)
        return res

    def str_professors(self):
        res = 'professors:\n'
        for p in self.professors:
            res += ' '.join(str(i) for i in p) + '\n'

        return res

    # setters

    def set_days(self, days):
        self.days = days
        return self

    def set_times(self, times):
        self.times = times
        return self

    def set_courses(self, courses, happiness):
        for i in range(courses):
            self.courses.append(Course(i, happiness[i]))
        return self

    def set_professors(self, professors):
        self.professors = professors
        return self

    def set_population(self, population):
        self.population = population
        return self

    def set_repeat(self, repeat):
        self.repeat = repeat
        return self

    # getters

    def get_days(self):
        return self.days

    def get_times(self):
        return self.times

    def get_courses(self):
        return self.courses

    def get_course(self, index):
        return self.courses[index]

    def get_professors(self):
        return self.professors

    def get_population(self):
        return self.population

    def get_repeat(self):
        return self.repeat

    # public methods

    def courses_size(self):
        return len(self.courses)

    def professors_size(self):
        return len(self.professors)

    def add_professor_to_course(self, index, professor):
        self.courses[index].add_professor(professor)
