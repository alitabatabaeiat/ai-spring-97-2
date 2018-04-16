class Class:

    # constructor

    def __init__(self, _id):
        self.id = _id
        self.day = -1
        self.time = -1
        self.professor = -1

    # For call to str(). Prints readable form

    def __str__(self):
        return 'Class Class:\n' + 'id = %i - day = %i - time = %i - professor = %i\n' % (self.id, self.day, self.time, self.professor)

    # setters

    def set_day(self, day):
        self.day = day
        return self

    def set_time(self, time):
        self.time = time
        return self

    def set_professor(self, professor):
        self.professor = professor
        return self

    # getters

    def get_id(self):
        return self.id

    def get_day(self):
        return self.day

    def get_time(self):
        return self.time

    def get_professor(self):
        return self.professor