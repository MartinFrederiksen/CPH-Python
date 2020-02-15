from Course import Course
from DataSheet import DataSheet
from Student import Student
import random
import csv

def generateStudents(number):
    students = []
    dataSheet = []
    grades = [-3, 00, 2, 4, 7, 10, 12]
    course1 = Course('Første semester', '103', 'BLA', 10, random.choice(grades))
    course2 = Course('Anden semester', '103', 'BLA', 10, random.choice(grades))
    course3 = Course('Tredje semester', '103', 'BLA', 10, random.choice(grades))
    course4 = Course('Python', '103', 'BLA', 10)
    courses = [course1, course2, course3, course4]

    names = ['Vikke', 'Asger', 'Emil', 'William', 'Alberte', 'Allan', 'Peter', 'Frank', 'Walter', 'James']
    genders = ['Male', 'Female']
    imgUrl = ['https://i.imgur.com/7ddcwox.png', 'https://i.imgur.com/brROJyA.jpg', 'https://i.imgur.com/PcHUlCH.jpg', 'https://i.imgur.com/jUYx9l5.jpg']

    for _ in range(number):
        for _ in range(random.randrange(len(courses))):
            dataSheet.append(random.choice(courses))
        students.append(Student(random.choice(names), random.choice(genders), DataSheet(dataSheet), random.choice(imgUrl)))
        dataSheet = []
    return students
#print([random.choice(names), random.choice(genders), DataSheet(courses), random.choice(imgUrl) for Student(name, gender, dataSheet, grade, imgUrl) in range(number)])  


def writeToCsv(number):
    with open('./students.csv', 'w') as File:
        writer = csv.writer(File, quoting=csv.QUOTE_NONNUMERIC)
        
        col = ['stud_name', 'gender' 'course_name', 'classroom', 'teacher', 'ECTS', 'grade', 'img_url']
        writer.writerow(col)

        students = generateStudents(number)
        for student in students:
            for course in student.dataSheet.courses:
                writer.writerow([
                    student.name,
                    student.gender,
                    course.name,
                    course.classroom,
                    course.teacher,
                    course.ECTS,
                    course.grade,
                    student.imgUrl
                    ])

def readFromCsv():
    students = {}
    with open('./students.csv', 'r') as File:
        reader = csv.reader(File)
        for row in list(reader)[1:]:
            if row[0] not in students:
                students[row[0]] = Student(row[0], row[1], DataSheet([Course(row[2], row[3], row[4], int(row[5]), int(row[6]) if row[6] else None)]), row[7])
            else:
                students[row[0]].dataSheet.courses.append(Course(row[2], row[3], row[4], int(row[5]), int(row[6]) if row[6] else None))
        return students