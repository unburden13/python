# employee_file = open("employees.txt", "r") --read - by default
# employee_file = open("employees.txt", "w") --write - overwrites - creates if not exist
# employee_file = open("employees.txt", "a") --append
# employee_file = open("employees.txt", "r+") --read and write
# print(employee_file.readable()) -- returns True or False

# print(employee_file.readline())  -- reads one line at a time
# print(employee_file.readlines()) -- reads all lines, returns a list
# print(employee_file.readlines()[1]) -- reads an specific line of the file
# print(employee_file.read()) -- reads the whole file, returns a string
# employee_file.seek(0) -- moves the cursor to the specified index

# pathlib module allows to handle paths on different operating systems - https://docs.python.org/3/library/pathlib.html


employee_file = open('employees.txt', 'r')
print(employee_file.readlines())
employee_file.close()

with open('employees.txt', 'a') as my_file:  # 'with' closes the file automatically ( no need to do file.close() )
    my_file.write('\nHilary - accountant')

