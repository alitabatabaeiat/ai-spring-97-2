class Course:

    # constructor

    def __init__(self, id, professor):
        self.id = id
        self.professor = professor

    # For call to str(). Prints readable form

    def __str__(self):
        return 'Course class:\n' + ('id = %i\n' % self.id) + ('professor = %i\n' % self.professor)

    # setters

    def set_professor(self, professor):
        self.professor = professor

    # getters

    def get_professor(self):
        return self.professor
