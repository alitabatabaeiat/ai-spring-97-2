from Schedule import Schedule
import operator


class Population:

    # constructor

    def __init__(self, db):
        self.db = db
        self.schedules = []

    def check(self):
        for schedule in self.get_schedules():
            schedule.check()

    # For call to str(). Prints readable form

    def __str__(self):
        res = '-----------------------\n'
        res += 'Population:\n' + self.str_schedules()
        res += '-----------------------'
        return res

    # str

    def str_schedules(self):
        res = 'schedules:\n'
        for schedule in self.get_schedules():
            res += str(schedule)
        return res

    # setters

    def set_schedule(self, index, schedule):
        self.schedules[index] = schedule.set_fitness()
        return self

    # getters

    def get_db(self):
        return self.db

    def get_population(self):
        return self.db.get_population()

    def get_schedule(self, index):
        return self.schedules[index]

    def get_schedules(self):
        return self.schedules

    def get_fittest(self):
        return self.sort().get_schedule(0)

    # public methods

    def generate(self):
        for i in range(self.get_population()):
            self.schedules.append(Schedule(self.db).fill_schedule().calculate_fitness())
        return self

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def schedules_size(self):
        return len(self.schedules)

    def sort(self):
        self.schedules.sort(key=operator.attrgetter('fitness'), reverse=True)
        return self



