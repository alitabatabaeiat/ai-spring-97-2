import random
# import FitnessCalc
from Course import SlotCourse
from copy import deepcopy


class Chromosome:

    # constructor

    def __init__(self, db, initialize=True):
        self.db = db
        self.courses = deepcopy(self.db.get_courses())
        self.fitness = 0
        self.genes = []  # genes[day][time][course] 3D-list
        for _ in range(self.db.get_days()):
            row = []  # empty day
            for _ in range(self.db.get_times()):
                row.append([])  # empty slots
            self.genes.append(row)

        if initialize:
            self.add_course_to_slots()

    # For call to str(). Prints readable form

    def __str__(self):
        res = '-----------------------\n'
        res += 'Chromosome Class:\n'
        res += 'fitness = %i\n' % self.fitness
        res += 'genes:\n' + self.str_genes()
        res += '-----------------------'
        return res

    # str

    def str_genes(self):
        res = ''
        for day in range(len(self.genes)):
            for time in range(len(self.genes[day])):
                res += '[ '
                for course in range(len(self.genes[day][time])):
                    res += '['
                    res += str(self.get_gene(day, time, course))
                    res += ']'
                    if course != len(self.genes[day][time]) - 1:
                        res += ' , '
                res += ' ]'
                if time != len(self.genes[day]) - 1:
                    res += ' - '
            res += '\n'

        return res

    def str_courses(self):
        res = 'courses:\n'
        for course in self.get_courses():
            res += str(course)
        return res

    # setters

    def set_gene(self, day, time, course, value):
        self.genes[day][time][course] = value
        self.fitness = 0

    def set_slot(self, day, time, courses):
        self.genes[day][time] = courses
        self.fitness = 0

    # getters

    def get_gene(self, day, time, course):
        return self.genes[day][time][course]

    def get_slot(self, day, time):
        return self.genes[day][time]

    def get_courses(self):
        return self.courses

    # public methods

    def courses_size(self):
        return len(self.courses)

    def add_new_course(self, day, time, course):
        self.genes[day][time].append(course)
        self.fitness = 0

    def get_fitness(self):
        # if self.fitness == 0:
        #     self.fitness = FitnessCalc.get_fitness(self)
        # return self.fitness
        return 1000

    def add_course_to_slots(self):
        while self.courses_size() > 0:
            self.put_a_course_on_any_slot()

    def put_a_course_on_any_slot(self):  # course number
        # get a random int for course to choose
        course_index = random.randint(0, self.courses_size() - 1)
        course = self.courses[course_index]

        for _ in range(self.db.get_repeat()):
            # get random day and time to put new course on this slot
            day = random.randint(0, self.db.get_days() - 1)
            time = random.randint(0, self.db.get_times() - 1)

            professors = self.get_professors_without_conflict(course, self.genes[day][time])
            if len(professors) > 0:
                # get a random int for professor index in professors without conflict
                professor_index = random.randint(0, len(professors) - 1)

                # get random professor from a course
                professor = professors[professor_index]

                # make new course for slot
                new_slot_course = SlotCourse(course.get_id(), professor)

                # add new course to slot
                self.add_new_course(day, time, new_slot_course)
                break

        # remove course from courses either selected or not
        del self.courses[course_index]

    def get_professors_without_conflict(self, course, slot):
        # course can not be duplicate because after choosing a course, it will be delete
        professors = list(course.get_professors())
        for slot_course in slot:
            for i in range(len(professors)):
                # remove each professor of the new course that is duplicate
                if slot_course.get_professor() == professors[i]:
                    del professors[i]
        return professors
