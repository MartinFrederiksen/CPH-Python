class Student():

    def __init__(self, name, gender, dataSheet, imgUrl):
        self.name = name
        self.gender = gender
        self.dataSheet = dataSheet
        self.imgUrl = imgUrl

    def getAvgGrade(self):
        if sum(filter(None, self.dataSheet.getGradesAsList())) == 0:
            return 0
        return sum(filter(None, self.dataSheet.getGradesAsList()))/len([i for i in self.dataSheet.getGradesAsList() if i])

    def showProgress(self):
        ects = 0
        for course in filter(None, self.dataSheet.courses):
            if course.ECTS > 0:
                ects += course.ECTS
        return (ects/150)*100

    def getCourses(self):
        return self.dataSheet.courses
        
    def __str__(self):
        return 'Name: {name}, Gender: {gender}, dataSheet: {dataSheet}, imgURL: {imgUrl}'.format(
                name=self.name, gender=self.gender, dataSheet=self.dataSheet, imgUrl=self.imgUrl)