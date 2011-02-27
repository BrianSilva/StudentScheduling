class Student:
    def __init__(self, Student_ID, First_Name, Last_Name, Sex, Grade, Birthday, Classes, Note):
        self.Student_ID = Student_ID
        self.First = First_Name
        self.setLast(Last_Name)
        self.setSex(Sex)
        self.Grade = Grade
        self.Birthday = Birthday
        Classes = {1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", }
        self.Classes = Classes
        self.Note = Note
    def setID(self, Student_ID):
        self.Student_ID = Student_ID
    def setFirst(self, First_Name):
        self.First = First_Name
        self.Name = self.First + " " + self.Last
    def setLast(self, Last_Name):
        self.Last = Last_Name
        self.Name = self.First + " " + self.Last
    def setSex(self, Sex):
        Male = ("male", "m", "boy", "b", "man")
        Female = ("female", "f", "girl", "g", "lady", "l", "woman")
        Sex = Sex.lower()
        if Sex in Male:
            Sex = "Male"
        elif Sex in Female:
            Sex = "Female"
        self.Sex = Sex
    def setGrade(self, Grade):
        self.Grade = Grade
    def setBirthday(self, Birthday):
        self.Birthday = Birthday
    def setClass(self, period, class1):
        self.Classes[period] = class1
    def setClasses(self, classes):
        self.Classes = tuple(classes)
    def setNote(self, Note):
        self.Note = Note
    def __str__(self):
        return "{0:<10}    {1:<30}  Grade: {2:>2}    Sex: {3}\n".format(self.Student_ID, self.Name, self.Grade, self.Sex)
    def details(self):
        string = self.__str__() + "\n"
        for i in self.Classes:
            string += str(i[1]) + " - " + i[0] + "\n"
        return string
    def compare(self, student2, fields):
        comparison = -1
        if fields[0] == "First":
            v1 = self.First.lower()
            v2 = student2.First.lower()
        elif fields[0] == "Last":
            v1 = self.Last.lower()
            v2 = student2.Last.lower()
        elif fields[0] == "Sex":
            v1 = self.Sex.lower()
            v2 = student2.Sex.lower()
        elif fields[0] == "Grade":
            v1 = self.Grade.lower()
            v2 = student2.Grade.lower()
        elif fields[0] == "Student_ID":
            v1 = self.Student_ID.lower()
            v2 = student2.Student_ID.lower()
        else:
            v1 = self.name.lower()
            v2 = student2.name.lower()
        if v1 < v2:
            comparison = -1
        elif v1 > v2:
            comparison = 1
        elif v1 == v2:
            if len(fields) == 1:
                comparison = 0
            else:
                comparison = self.compare(student2, fields[1:])
        return comparison
