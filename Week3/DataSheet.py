class DataSheet():

    def __init__(self, courses):
        self.courses = courses

    def getGradesAsList(self):
        return [course.grade for course in self.courses]

    def __str__(self):
        return 'Course: {name}'.format(
            name=self.courses)