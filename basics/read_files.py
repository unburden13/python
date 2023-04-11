# employee_file = open("employees.txt", "r") --read
# employee_file = open("employees.txt", "w") --write - overwrites
# employee_file = open("employees.txt", "a") --append
# employee_file = open("employees.txt", "r+") --read and write
employee_file = open("employees.txt", "r")
print(employee_file.readable())

# print(employee_file.readline())  -- reads one line at a time
# print(employee_file.readlines()) -- reads all lines, returns a list
# print(employee_file.readlines()[1]) -- reads an specific line of the file
# print(employee_file.read()) -- reads the whole file, returns a string

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

append_employee_file = open("employees.txt", "a")
append_employee_file.write("\nHilary - accountant")
append_employee_file.close()

