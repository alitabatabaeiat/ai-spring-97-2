class Database:

    # constructor
    def __init__(self):
        self.days = 0
        self.times = 0
        self.happiness = []
        self.professors = []
        self.sadness = []

    # For call to str(). Prints readable form

    def __str__(self):
        res = 'Database:\n'
        res += 'days = %i\n' % self.days
        res += 'times = %i\n' % self.times
        res += self.str_happiness()
        res += self.str_professors()
        res += self.str_sadness()

        return res

    # str

    def str_happiness(self):
        return 'happines:\n' + ' '.join(str(i) for i in self.happiness) + '\n'

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

    def set_happiness(self, happiness):
        self.happiness = happiness

    def set_professors(self, professors):
        self.professors = professors

    def set_sadness(self, sadness):
        self.sadness = sadness

    # getters

    def get_days(self):
        return self.days

    def get_times(self):
        return self.times

    def get_courses(self):
        return len(self.happiness)

    def get_happiness(self):
        return self.happiness

    def get_professors_number(self):
        return len(self.professors)

    def get_professors(self):
        return self.professors

    def get_sadness(self):
        return self.sadness