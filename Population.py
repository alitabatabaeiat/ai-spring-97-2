from Schedule import Schedule


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
        self.schedules[index] = schedule
        return self

    # getters

    def get_population(self):
        return self.db.get_population()

    def get_schedule(self, index):
        return self.schedules[index]

    def get_schedules(self):
        return self.schedules

    def get_fittest(self):
        fittest = self.get_schedule(0)

        for i in self.schedules:
            if fittest.get_fitness() < i.get_fitness():
                fittest = self.get_schedule(i)

        return fittest

    # public methods

    def generate(self):
        for i in range(self.get_population()):
            self.schedules.append(Schedule(self.db).initialize())
        return self
