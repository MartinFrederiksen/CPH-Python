class Course():

    def __init__(self, name, classroom, teacher, ECTS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade


    def __str__(self):
        return 'Name: {name}, Classroom: {classroom}, Teacher: {teacher}, ECTS: {ects}, Grade: {grade}'.format(
            name=self.name, classroom=self.classroom, teacher=self.teacher, ects=self.ECTS, grade=self.grade)