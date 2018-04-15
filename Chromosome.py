import random
# import FitnessCalc
from Course import Course


class Chromosome:

    # constructor

    def __init__(self, db):
        self.db = db
        self.courses = list(self.db.get_courses())
        self.fitness = 0
        self.genes = []  # genes[day][time][course] 3D-list
        for _ in range(self.db.get_days()):
            row = [] # empty day
            for _ in range(self.db.get_times()):
                row.append([]) # empty slots
            self.genes.append(row)

    # For call to str(). Prints readable form

    def __str__(self):
        res = 'Chromosome Class:\n' + str(self.db)
        res += 'fitness = %i\n' % self.fitness
        res += 'genes:\n' + str(self.genes)
        return res

    # setters

    def set_gene(self, day, time, course, value):
        self.genes[day][time][course] = value
        self.fitness = 0

    # getters

    def get_gene(self, day, time, course):
        return self.genes[day][time][course]

    def get_courses_size(self):
        return len(self.courses)

    # public methods

    def get_fitness(self):
        # if self.fitness == 0:
        #     self.fitness = FitnessCalc.get_fitness(self)
        # return self.fitness
        return 1000

    def add_course_to_slot(self):
        state = 0
        while self.get_courses_size() > 0:
            index = random.randint(1, self.get_courses_size())
            if state == 0:
                result = self.put_course_on_first_available_slot(index)
                if not result:
                    state = 1
                    continue
                del self.courses[index]

            elif state == 1:
                result = self.put_course_on_any_slot(index)
                if not result:
                    print('There is No Chance to put remaining courses into table!\n')



    def put_course_on_first_available_slot(self, index):
        professor_index = random.randint(0, len(self.courses[index]) - 1)
        professor = self.courses[index][professor_index]
        new_course = Course(index, professor)

        for day in self.db.get_days():
            for time in self.db.get_times():
                if len(self.genes[day][time]) == 0:
                    self.genes[day][time].append(new_course)
                    return True
        return False

    def put_course_on_any_slot(self, index):
        pass

    def has_conflict(self, index, slot):
        conflict = True
        professors = self.courses[index]
        for s in slot:
            for i in range(len(professors)):
                if s.get_professor() == professors[i]: # remove each professor of the new course that is duplicate
                    del professors[i]
                else:
                    conflict = False

        return conflict

