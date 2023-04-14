from OOP.Student import Student
from OOP.Student import ClassAssistant
from OOP.Student import LibraryAssistant
from OOP.Student import SuperStudent

student1 = Student("Bob", "Art", 3.2, 11111, False)
student2 = Student("Barbara", "Architecture", 22222, 4.6, True)
student3 = Student("Michael", "Biology", 2, 33333, True)


student1.get_info()
student2.get_info()
# student3.get_info()


def get_higher_gpa(*args):
    return max(args)


print(f'Higher gpa of all students is {get_higher_gpa(student1.gpa, student2.gpa, student3.gpa)}')

student4 = student1.get_dummy(student1.gpa)
student5 = Student.get_dummy(4)
print(student5.gpa)

assistant = ClassAssistant('Math', '2023/01/01', 'Tom', 'Science', 4.5, 00000)
print(assistant.replace_teacher())


super_student = SuperStudent('Physics', 'Arts', '2023/01/01', 'Gustav', 'Politics', 5, 77777)
print(f'super student : {super_student.work_on_stand()}')
print(f'super student : {super_student.replace_teacher()}')

