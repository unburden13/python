class Student:
    # Class object attribute --> static, same value for all objects.
    # Any change will reflect to other instances.
    membership = False

    def __init__(self, name, major, gpa, pwd, is_on_probation=False):
        # Instance attribute --> dynamic, specific to object
        # Changes will not reflect to other instances
        self.name = name
        self.major = major
        self.gpa = gpa
        self._pwd = pwd  # underscore is a convention for 'private', there's no true privacy in python.
        if gpa > 3:
            Student.membership = True  # this change will reflect to all objects
            self.is_on_probation = is_on_probation
            # if gpa <= 3, self.is_on_probation will not be created, so will throw an error on the program if it's used

    def get_info(self):
        print(f'{self.name}\nmajor: {self.major}\ngpa: {self.gpa}\nis on probation: {self.is_on_probation}\n')

    # @classmethod
    # receives the class (not an instance) as first argument.
    # class and its properties can be used inside the method.
    # callable without instantiating the class.
    # useful to create an instance of a class with some sort of pre-processing.
    @classmethod
    def get_dummy(cls, some_gpa):
        return cls('Dummy student', 'none', 00000, some_gpa - 1)

    # @staticmethod
    # gets no implicit first argument.
    # callable without instantiating the class.
    @staticmethod
    def do_something(num1, num2):
        return num1 * num2


class ClassAssistant(Student):  # inheritance
    def __init__(self, subject, start_date, name, major, gpa, pwd):
        Student.__init__(self, name, major, gpa, pwd)
        self.subject = subject
        self.start_date = start_date

    def replace_teacher(self):
        return f'Currently teaching {self.subject}'


class LibraryAssistant(Student):  # inheritance
    def __init__(self, section, start_date, name, major, gpa, pwd):
        Student.__init__(self, name, major, gpa, pwd)
        # can also use super().__init__() - but could be problematic for multiple inheritance and MRO
        self.section = section
        self.start_date = start_date

    def work_on_stand(self):
        return f'Currently working on stand of section {self.section}'


class SuperStudent(ClassAssistant, LibraryAssistant):  # multiple inheritance
    def __init__(self, subject, section, start_date, name, major, gpa, pwd):
        ClassAssistant.__init__(self, subject, start_date, name, major, gpa, pwd)
        LibraryAssistant.__init__(self, section, start_date, name, major, gpa, pwd)

