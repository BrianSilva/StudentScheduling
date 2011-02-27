#  Added the importer def and supporting imports and menu modifications
#       def importer(self) is a modified copy of your orginal def add(self)
#       def importer(self) will: 
#       -open and read a csv (comma delimited file) named stu.csv from the application directory
#       -parse the comma delimited fields and assign to variables
#       -call the newStudent function 
#       -print each student it adds
#       -close csv
#       -exit back to the menu

import os
import time
from time import strftime
import pickle
import hashlib
import csv              # Added to support import parsing CSV from fakenamegenerator.com
import random           # Added to support random selecting a grade 9-12 during import of students
from Classes import *
try:
 from Renew import *
except:
    pass
class SchoolDB (list):
    def __init__(self, name, year, Database_File_Location):
        list.__init__(self)
        self.School_Name = name
        self.School_Year = year
        self.Database_File_Location = Database_File_Location
        self.save()
    def save(self):
        file = open(self.Database_File_Location, 'wb')
        pickle.dump(self, file)
        file.close()
    def addStudent(self, student):
        self.append(student)
        self.save()
    def newStudent(self, Student_ID, First_Name, Last_Name, Sex, Grade, Birthday, Classes, Note):
        self.append(Student(Student_ID, First_Name, Last_Name, Sex, Grade, Birthday, Classes, Note))
        self.save()
    def deleteStudent(self, student):
        self.remove(student)
        self.save()
    def printStudents(self):
        found = False
        count = 1
        if len(self) == 0:
            print("No students found")
            found = False
        else:
            for i in self:
                print("{0:>4}:  {1}".format(count, i))
                count+=1
                found = True
        return found
    def searchStudents(self, searchString):
        searchString = searchString.lower()
        matches = []
        for i in self:
            if i.First.lower().find(searchString) >= 0:
                matches.append(i)
            elif i.Last.lower().find(searchString) >= 0:
                matches.append(i)
            elif i.Sex.lower().find(searchString) >= 0:
                matches.append(i)
            elif i.Grade.lower().find(searchString) >= 0:
                matches.append(i)
            elif i.Student_ID.lower().find(searchString) >= 0:
                matches.append(i)
        return matches
    def replaceStudent(self, student1, student2):
        successful = False
        try:
            i = self.index(student1)
            self[i] = student2
            self.save()
            successful = True
        except:
            successful = False
        finally:
            return successful
    def sort(self, fields):
        length = len(self)
        if length > 1:
            for i in range(length):
                for j in range(i+1, length):
                    q = self[i].compare(self[j], fields)
                    if q > 0:
                        self.insert(i, self[j])
                        del self[j+1]
        self.save()
class Main_GUI:
    def __init__(self):
        self.DB = ""
    def setDB(self, DB):
        self.DB = DB
    def Intro(self):
        directory = os.getcwd()
        pyc_location = "/Renew.pyc"
        pyc_check = os.path.isfile(directory + pyc_location)
        if pyc_check == True:
            os.remove(directory + pyc_location)
        else:
            pass
        self.Clear()
        print("""
+------------------------------------------------+
|                STUDENT DATABASE                |
+------------------------------------------------+
|                                                |
|  SS Database                      Version 0.8  |
|                                                |
|        Programmed By: Baskett, Kenny           |
|                       Bruton, Rob              |
|                       Silva, Brian             |
|                                                |
+------------------------------------------------+""")
        time.sleep(1)
        self.Clear()
    def Menu(self):
        keepRunning = True
        directory = os.getcwd()
        pyc_location = "/Renew.pyc"
        pyc_check = os.path.isfile(directory + pyc_location)
        if pyc_check == True:
            os.remove(directory + pyc_location)
        else:
            pass
        self.Clear()
        print("""
+------------------------------------------------+
|             STUDENT DATABASE MENU              |
+------------------------------------------------+
|                                                |
|  [V] View Student List  [A] Add a Student      |
|  [S] Search Students    [M] Management         |
|  [F] Filter Display     [Q] Quit               |
|                                                |
|                                                |
|       [I] Import Student File                  |
+------------------------------------------------+
""")                                            #   Added the I menu item
        mInput = input(">> ")
        if mInput.lower() == "v":
            self.Clear()
            self.View()
        elif mInput.lower() == "s":
            self.Clear()
            self.search()
        elif mInput.lower() == "a":
            self.add()
        elif mInput.lower() == "f":
            self.sort()
        elif mInput.lower() == "m":
            self.databaseMenu2()
        elif mInput.lower() == "i":             # added the else if for I
            self.Clear()
            self.importer()
        elif mInput == "q":
            try:
                directory = os.getcwd()
                pyc_location = "/Renew.pyc"
                pyc_check = os.path.isfile(directory + pyc_location)
                if pyc_check == True:
                    os.remove(directory + pyc_location)
                else:
                    pass
                quit()
            except:
                self.Menu()
        elif mInput == "":
            self.Menu()
        else:
            print("Invalid selection.")
            time.sleep(1)
            self.Clear()
            self.Menu()
    def noSettings(self):
        print("Settings file not found...")
        time.sleep(1)
        self.databaseMenu1()
    def noDatabase(self):
        print("Specified database not found...")
        time.sleep(1)
        self.databaseMenu1()
    def databaseMenu1(self):
        runningCheck = True
        while runningCheck == True:
            self.Clear()
            print("[C] Create database")
            print("[Q] Quit")
            choice = input("\n>> ")
            if choice.lower() == "c":
                firstRun = os.path.isfile("Do_Not_Modify.dat")
                if firstRun == True:
                    firstRunSettings = os.path.isfile("Settings.ini")
                    if firstRunSettings == True:
                        retrieve1 = self.License_Check_1("Settings.ini")
                        retrieve2 = self.License_Check_2("Do_Not_Modify.dat")
                        if retrieve1 == retrieve2:
                            if self.newDatabase() == False:
                                print("Unsuccessful")
                                print("Restart the program to try again.")
                                time.sleep(1)
                                self.Clear()
                                runningCheck == False
                            else:
                                self.Menu()
                        else:
                            print("Corrupt file or invalid license.")
                            time.sleep(1)
                            self.Clear()
                            runningCheck == False
                    else:
                        print("Corrupt/missing/invalid file or database has already been created.")
                        time.sleep(1)
                        self.Clear()
                        runningCheck == False
                else:
                    print("Corrupt/missing/invalid file or database has already been created.")
                    time.sleep(1)
                    self.Clear()
                    runningCheck == False
            elif choice.lower() == "ssr":
                self.Clear()
                code = input("Renew Code: ")
                if code == "":
                    self.databaseMenu1()
                else:
                    if Renew_License().run(code) == False:
                        runningCheck == False
                    else:
                        self.Clear()
                        print("Update successful!")
                        print("The program will reload itself in 5 seconds...")
                        time.sleep(5)
            elif choice.lower() == "q":
                try:
                    quit()
                except:
                    self.databaseMenu1()
            elif choice == "":
                self.databaseMenu1()
            else:
                print("Invalid selection.")
                time.sleep(1)
                self.databaseMenu1()
        if runningCheck == True:
            self.databaseMenu1()
        else:
            self.Clear()
    def databaseMenu2(self):
        self.Clear()
        print("""
+------------------------------------------------------------------------------+
|  School Database Information                                                 |
+------------------------------------------------------------------------------+
|  School Name: {0:<34}  School Year: {1:<12}  |
|  Database File Location: {2:<50}  |
+------------------------------------------------------------------------------+

[E] Edit database info
[W] Wipe database
[X] Cancel
""".format(self.DB.School_Name, self.DB.School_Year, self.DB.Database_File_Location))
        mInput = input(">> ")
        if mInput.lower() == "e":
            print("Feature coming soon!")
            time.sleep(1)
            self.databaseMenu2()
        elif mInput.lower() == "w":
            if self.Wipe_Database() == True:
                self.Clear()
                print("Database successfully wiped.")
                time.sleep(1)
                self.Menu()
            else:
                self.databaseMenu2()
        elif mInput.lower() == "x":
            self.Menu()
        elif mInput == "":
            self.databaseMenu2()
        else:
            print("Invalid selection.")
            time.sleep(1)
            self.databaseMenu2()
    def Wipe_Database(self):
        self.Clear()
        wiped = False
        print("Are you sure you want to wipe the database? (Y/N)")
        confirm = input(">> ")
        if confirm.lower() == "y":
            try:
                name = ""
                year = ""
                path = os.getcwd()
                path2 = path + "/Settings.ssc"
                path += "/Database.ssd"
                os.remove(path)
                os.remove(path2)
                s = Settings(path)
                DB = SchoolDB(name, year, path)
                self.setDB(DB)
                wiped = True
            except:
                wiped = False
        elif confirm.lower() == "n":
            wiped = False
        elif confirm == "":
            self.Wipe_Database()
        else:
            print("Invalid selection.")
            time.sleep(1)
            self.Wipe_Database()
        return wiped
    def newDatabase(self):
        success = False
        try:
            name = ""
            year = ""
            path = os.getcwd()
            path += "/Database.ssd"
            s = Settings(path)
            DB = SchoolDB(name, year, path)
            self.setDB(DB)
            file1 = "Settings.ini"
            file2 = "Do_Not_Modify.dat"
            os.remove(file1)
            os.remove(file2)
            success = True
        except:
            success = False
        return success
    def add(self):
        self.Clear()
        print("Please fill in the following information.\n")
        Student_ID = input("   ID Number: ")
        First_Name = input("  First Name: ")
        Last_Name = input("   Last Name: ")
        Sex = input("         Sex: ")
        Grade = input("       Grade: ")
        Birthday = ""
        Note = ""
        print("\n")
        self.DB.newStudent(Student_ID, First_Name, Last_Name, Sex, Grade, Birthday, {}, Note)
        print(First_Name + " " + Last_Name + " has been added to the database.")
        time.sleep(1)
        self.Clear()
        self.Menu()
                                                        # Added the importer
    def importer(self):
        self.Clear()
        random.seed()
        print("Student file will be imported.\n")
        #inputIDX = input("\n\n\n\n   Please Enter the Starter Student ID: ")  #for testing
        #idx = int(inputIDX)  #for testing
        csvFile = open("stu.csv", 'r')
        reader = csv.reader(csvFile)
        for row in reader:
            #idx = idx +1  #for testing
            #Student_ID = idx   #for testing
            Student_ID, First_Name, Last_Name, Sex, Birthday = row
            Grade = random.randint(9,12)
            Note = ""
            self.DB.newStudent(Student_ID, First_Name, Last_Name, Sex, Grade, Birthday, {}, Note)
            print(First_Name + " " + Last_Name + " has been added to the database.\n")
        csvFile.close()
        time.sleep(1)
        self.Clear()
        self.Menu()
    def search(self):
        print("Please enter what you would like to search for.\n")
        searchQuery = input("Query: ")
        print("\n")
        print("{0:^79}".format("RESULTS"))
        print("-"*79)
        matches = self.DB.searchStudents(searchQuery)
        if len(matches) == 0:
            print("No students matched the search query.")
            time.sleep(1)
            self.Menu()
        else:
            count = 1
            for i in matches:
                print("{0:>4}:  {1}".format(count, i))
                count+=1
            self.editMenu(matches)
        self.Clear()
    def View(self):
        self.Clear()
        print("{0:^79}".format("STUDENTS"))
        print("-"*79)
        if self.DB.printStudents() == True:
            self.editMenu(self.DB)
        else:
            time.sleep(1)
            self.Menu()
    def sort(self):
        self.Clear()
        fields = []
        fields2 = ""
        d = {"1":"Student_ID", "2":"First", "3":"Last", "4":"Sex", "5":"Grade"}
        print("Sort by:")
        print("[1] Student ID")
        print("[2] First Name")
        print("[3] Last Name")
        print("[4] Sex")
        print("[5] Grade")
        print("[X] Cancel")
        print("\nEnter the fields you wish to sort by.")
        print("Enter X to cancel.")
        print("Press Enter to sort.")
        mInput = "a"
        while (mInput != "" and mInput != "x"):
            mInput = input(">> ")
            mInput = mInput.lower()
            if (mInput != "" and mInput != "x"):
                if mInput in d.keys():
                    fields.append(d[mInput])
                    fields2 = fields2 + d[mInput] + ">"
                else:
                    print("Invalid selection.")
        if mInput.lower() == "x":
            self.Menu()
        if mInput == "":
            print("Sorting by {0}".format(fields2))
            time.sleep(1)
            self.DB.sort(fields)
            self.View()
    def Clear(self):
        print("\n" * 80)
    def editMenu(self, students):
        keepRunning = False
        print("\n\nEnter a student number to view/edit that student.")
        print("[X] Cancel\n")
        Edit_StudentNum = input(">> ")
        if Edit_StudentNum != "x":
            if Edit_StudentNum == "":
                self.View()
            else:
                try:
                    s1 = students[int(Edit_StudentNum) - 1]
                    s2 = self.Edit_Student(s1)
                    if s2 == "delete":
                        self.DB.deleteStudent(s1)
                        print("Student deleted")
                        time.sleep(1)
                        self.View()
                    elif s2 == True:
                        self.DB.replaceStudent(s1, s2)
                        self.Clear()
                        print("Student updated.")
                        time.sleep(1)
                        self.View()
                    else:
                        self.View()
                except:
                    print("\n\nInvalid selection.")
                    time.sleep(1)
                    self.View()
        self.Menu()
    def Edit_Student(self, student):
        self.Clear()
        print("""
+------------------------------------------------------------------------------+
|  [I] Student ID: {0:<15}  [1] Period 1: {6:<27}  |
|  [F] First Name: {1:<15}  [2] Period 2: {7:<27}  |
|  [L]  Last Name: {2:<15}  [3] Period 3: {8:<27}  |
|  [S]        Sex: {3:<15}  [4] Period 4: {9:<27}  |
|  [G]      Grade: {4:<15}  [5] Period 5: {10:<27}  |
|  [B]   Birthday: {5:<15}  [6] Period 6: {11:<27}  |
|  [A] All Periods                  [7] Period 7: {12:<27}  |
|  [C] Clear Periods                [8] Period 8: {13:<27}  |
| -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - |
|  [N] Note: {14:<64}  |
|  [SS] Schedule:  {15:<59}  |
+------------------------------------------------------------------------------+
""".format(student.Student_ID, student.First, student.Last, student.Sex, student.Grade, student.Birthday, student.Classes[1], student.Classes[2], student.Classes[3], student.Classes[4], student.Classes[5], student.Classes[6], student.Classes[7], student.Classes[8], student.Note, ""))
        print("\nChoose the letter/number of the field you wish to edit.")
        print("Enter D to delete the student from the database.")
        print("[X] Cancel\n")
        mInput = input(">> ")
        if mInput.lower() == "i":
            student.setID(input("Student ID: "))
        elif mInput.lower() == "ss":
            d = strftime("%A, %B %d")
            t = strftime("%r")
            print("""
+------------------------------------------------------------------------------+
|  {0:^74}  |
+ -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - +
|  {1:<36}  {2:>36}  |
|  {3:<36}  {4:>36}  |
|                                                                              |
|                                                                              |
|  {5:<13}  {6:<35}  {7:<5}  {8:<15}  |
|  {9:<13}  {10:<35}  {11:<5}  {12:<15}  |
|  {13:<13}  {14:<35}  {15:<5}  {16:<15}  |
|  {17:<13}  {18:<35}  {19:<5}  {20:<15}  |
+------------------------------------------------------------------------------+
""".format("Rockdale Magnet School", d, student.First + " " + student.Last, t, "Homeroom: " + student.Classes[1], "Period:", "Course Name:", "Rm #:", "Teacher:", "1st Period:", Class.className))
            input()
        elif mInput.lower() == "f":
            student.setFirst(input("First Name: "))
        elif mInput.lower() == "l":
            student.setLast(input("Last Name: "))
        elif mInput.lower() == "s":
            student.setSex(input("Sex: "))
        elif mInput.lower() == "g":
            student.setGrade(input("Grade: "))
        elif mInput.lower() == "b":
            student.setBirthday(input("Birthday: "))
        elif mInput.lower() == "a":
          student.setClass(1, input("Period 1: "))
          student.setClass(2, input("Period 2: "))
          student.setClass(3, input("Period 3: "))
          student.setClass(4, input("Period 4: "))
          student.setClass(5, input("Period 5: "))
          student.setClass(6, input("Period 6: "))
          student.setClass(7, input("Period 7: "))
          student.setClass(8, input("Period 8: "))
        elif mInput.lower() == "c":
          student.setClass(1, "")
          student.setClass(2, "")
          student.setClass(3, "")
          student.setClass(4, "")
          student.setClass(5, "")
          student.setClass(6, "")
          student.setClass(7, "")
          student.setClass(8, "")
        elif mInput == "1":
          student.setClass(1, input("Period 1: "))
        elif mInput == "2":
          student.setClass(2, input("Period 2: "))
        elif mInput == "3":
          student.setClass(3, input("Period 3: "))
        elif mInput == "4":
          student.setClass(4, input("Period 4: "))
        elif mInput == "5":
          student.setClass(5, input("Period 5: "))
        elif mInput == "6":
          student.setClass(6, input("Period 6: "))
        elif mInput == "7":
          student.setClass(7, input("Period 7: "))
        elif mInput == "8":
          student.setClass(8, input("Period 8: "))
        elif mInput.lower() == "n":
          student.setNote(input("Note: "))
        elif mInput.lower() == "d":
          student = "delete"
        elif mInput.lower() == "x":
          student = False
        elif mInput == "":
          self.Edit_Student(student)
        else:
          print("Invalid selection.")
          time.sleep(1)
          self.Edit_Student(student)
        return student
    def License_Check_1(self, file):
        self.file = file
        f = open(file, "rb")
        full_hash = pickle.load(f)
        f.close()
        #for line in o:
        #    md5_line = hashlib.md5()
        #    md5_line.update(bytes(line, encoding = "utf8"))
        #    full_hash += md5_line.hexdigest() + "\n"
        full_hash = str(full_hash)
        return full_hash
    def License_Check_2(self, file):
        self.file = file
        f = open(file, "r")
        full_hash = f.read()
        f.close()
        full_hash = str(full_hash)
        return full_hash
class Settings:
    def __init__(self, DBPath):
        self.DBPath = DBPath
        self.save()
    def __str__(self):
        return "Database Path:  {0}".format(self.DBPath)
    def save(self):
        file = open("Settings.ssc", 'wb')
        pickle.dump(self, file)
        file.close()
def getSettings():
        checkSettings = os.path.isfile("Settings.ssc")
        if checkSettings:
            f = open("Settings.ssc", "rb")
            s = pickle.load(f)
            f.close()
        else:
            s = False
        return s

directory = os.getcwd()
pyc_location = "/Renew.pyc"
pyc_check = os.path.isfile(directory + pyc_location)
if pyc_check == True:
    os.remove(directory + pyc_location)
else:
    pass
Main_GUI = Main_GUI()
Main_GUI.Intro()
settings = getSettings()
if settings == False:
    Main_GUI.noSettings()
else:
    path = settings.DBPath
    fCheckAction  = os.path.isfile(path)
    if fCheckAction == False:
        Main_GUI.noDatabase()
    else:
        f = open(path, "rb")
        DB = pickle.load(f)
        f.close()
        Main_GUI.setDB(DB)
    Main_GUI.Menu()
