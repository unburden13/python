class Student:
    # Class object attribute --> static, same value for all objects.
    # Any change will reflect to other instances.
    membership = True

    def __init__(self, name, major, gpa, is_on_probation=False):
        # Instance attribute --> dynamic, specific to object
        # Changes will not reflect to other instances
        self.name = name
        self.major = major
        self.gpa = gpa
        if gpa > 3:
            Student.membership = False  # this change will reflect to all objects
            self.is_on_probation = is_on_probation
            # self.is_on_probation will not be created, so will throw an error on the program if it's used

    def get_info(self):
        print(f'{self.name}\nmajor: {self.major}\ngpa: {self.gpa}\nis on probation: {self.is_on_probation}\n')

    # @classmethod
    # receives the class (not an instance) as first argument.
    # class and its properties can be used inside the method.
    # callable without instantiating the class.
    # useful to create an instance of a class with some sort of pre-processing.
    @classmethod
    def get_dummy(cls, some_gpa):
        return cls('Dummy student', 'none', some_gpa - 1)

    # @staticmethod
    # gets no implicit first argument.
    # callable without instantiating the class.
    @staticmethod
    def do_something(num1, num2):
        return num1 * num2
