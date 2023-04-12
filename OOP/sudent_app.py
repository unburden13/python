from OOP.Student import Student

student1 = Student("Bob", "Art", 3.2, False)
student2 = Student("Barbara", "Architecture", 4.6, True)
student3 = Student("Michael", "Biology", 2, True)


student1.get_info()
student2.get_info()
# student3.get_info()


def get_higher_gpa(*args):
    return max(args)


print(f'Higher gpa of all students is {get_higher_gpa(student1.gpa, student2.gpa, student3.gpa)}')

student4 = student1.get_dummy(student1.gpa)
student5 = Student.get_dummy(4)
print(student5.gpa)

