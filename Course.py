class Course:

    # constructor

    def __init__(self, _id, happiness):
        self.id = _id + 1
        self.happiness = happiness
        self.sadness = []
        self.professors = []

    # For call to str(). Prints readable form

    def __str__(self):
        return 'Course: ' + ('id = %i - ' % self.id) + ('happiness = %i - ' % self.happiness)\
               + ('sadness = %i - ' % str(self.sadness)) + ('professors = %s' % str(self.professors)) + '\n'

    # setters

    def set_sadness(self, sadness):
        self.sadness = sadness
        return self

    # getters

    def get_id(self):
        return self.id

    def get_happiness(self):
        return self.happiness

    def get_sadness(self, index):
        return self.sadness[index]

    def get_professors(self):
        return self.professors

    def get_professor(self, index):
        return self.professors[index]

    # public methods

    def add_professor(self, index):
        self.professors.append(index)

    def remove_professor(self, index):
        del self.professors[index]

    def professors_size(self):
        return len(self.professors)


class SlotCourse:

    # constructor

    def __init__(self, _id, professor):
        self.id = _id
        self.professor = professor

    # For call to str(). Prints readable form

    def __str__(self):
        return 'SlotCourse class: ' + ('id = %i - ' % self.id) + ('professor = %i' % self.professor)

    # setters

    def set_professor(self, professor):
        self.professor = professor

    # getters

    def get_id(self):
        return self.id

    def get_professor(self):
        return self.professor
