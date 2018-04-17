class Class:

    # constructor

    def __init__(self, _id, course):
        self.id = _id
        self.course = course
        self.slot = None
        self.professor = -1

    # For call to str(). Prints readable form

    def __str__(self):
        return 'Class %i:\tday = %i \ttime = %i \tprofessor = %i\n' % \
               (self.get_id(), self.get_slot().get_day(), self.get_slot().get_time(), self.get_professor())

    # setters

    def set_slot(self, slot):
        self.slot = slot
        return self

    def set_professor(self, professor):
        self.professor = professor
        return self

    # getters

    def get_id(self):
        return self.id

    def get_course(self):
        return self.course

    def get_slot(self):
        return self.slot

    def get_professor(self):
        return self.professor
