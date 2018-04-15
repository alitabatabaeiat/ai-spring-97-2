class Course:

    # constructor

    def __init__(self):
        self.professors = []

    # For call to str(). Prints readable form

    def __str__(self):
        return ' '.join(str(i) for i in self.professors) + '\n'

    # getters

    def get_professors(self):
        return self.professors

    # public methods

    def add_professor(self, professor):
        self.professors.append(professor)