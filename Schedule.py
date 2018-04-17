import random
# import FitnessCalc
from Class import Class
from copy import deepcopy


class Schedule:

    # constructor

    def __init__(self, db):
        self.db = db
        self.courses = deepcopy(self.db.get_courses())
        self.fitness = 0
        self.classes = []

    def check(self):
        for i in range(self.classes_size()):
            for j in range(self.classes_size()):
                if i == j:
                    break
                if self.get_class(i).get_slot().is_equal_slot(self.get_class(j).get_slot()) and self.get_class(i).get_professor() == self.get_class(j).get_professor():
                    print('CONFLICT')

    # For call to str(). Prints readable form

    def __str__(self):
        res = '-----------------------\n'
        res += 'Schedule:\n'
        res += '\tfitness = %i\n' % self.fitness
        res += '\tclasses: \n%s\n' % self.str_classes()
        res += '-----------------------'
        return res

    # str

    def str_classes(self):
        res = ''
        for _class in self.get_classes():
            res += '\t\t%s' % str(_class)
        return res

    def str_courses(self):
        res = 'courses:\n'
        for course in self.get_courses():
            res += str(course)
        return res

    # setters

    def set_class(self, index, _class):
        self.classes[index] = _class
        self.fitness = 0
        return self

    # getters

    def get_classes(self):
        return self.classes

    def get_class(self, index):
        return self.classes[index]

    def get_courses(self):
        return self.courses

    def get_random_course(self):
        return self.courses[random.randint(0, self.courses_size() - 1)]

    # public methods

    def add_class(self, _class):
        self.classes.append(_class)

    def classes_size(self):
        return len(self.get_classes())

    def initialize(self):
        while len(self.courses) > 0:
            course = self.get_random_course()
            for _ in range(self.db.get_repeats()):
                new_class = Class(course.get_id(), course)
                new_class.set_slot(self.db.get_random_slot())
                professors = self.get_professors_without_conflict_on_slot(course, new_class.get_slot())
                if len(professors) > 0:
                    new_class.set_professor(professors[random.randint(0, len(professors) - 1)])
                    self.add_class(new_class)
                    break
            self.remove_course(course)
        return self

    def get_professors_without_conflict_on_slot(self, course, slot):
        # course can not be duplicate because after choosing a course, it will be delete
        professors = list(course.get_professors())
        for _class in self.get_classes():
            if _class.get_slot().is_equal_slot(slot):
                # remove each professor of the new course that is duplicate
                professors = [x for x in professors if x != _class.get_professor()]
        return professors

    def courses_size(self):
        return len(self.courses)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_fitness(self):
        # if self.fitness == 0:
        #     self.fitness = FitnessCalc.get_fitness(self)
        # return self.fitness
        return 1000
