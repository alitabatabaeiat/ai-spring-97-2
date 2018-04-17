class Slot:

    # constructor

    def __init__(self, day, time):
        self.day = day
        self.time = time

    # For call to str(). Prints readable form

    def __str__(self):
        return 'Slot: day = %i - time = %i\n' % (self.get_day(), self.get_time())

    # getters

    def get_day(self):
        return self.day

    def get_time(self):
        return self.time

    # public methods

    def is_equal_slot(self, slot):
        if self.get_day() == slot.get_day() and self.get_time() == slot.get_time():
            return True
        return False
