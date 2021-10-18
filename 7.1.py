"""
7.1 Grade entry

Get the total amount of students that need to be graded
After that get the students name and grade and display that in the input
"""


def main():
    grades = []
    num_students = int(input("How many students do you you need to enter grades for? "))
    for students in range(1, num_students + 1):
        name = input("What is the name of the student? ")
        grade = input("What is the grade of the student ")
        student_grade = [name, grade]
        grades.append(student_grade)
    print(grades)

    file = open('grades.txt', 'w')
    for line in grades:
        line_out = "'" + line[0] + "','" + line[1] + "'\n"
        file.writelines(line_out)
    file.close()


main()
