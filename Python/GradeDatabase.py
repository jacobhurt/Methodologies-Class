#
# GradeDatabase.py
# 
# Author:          Adopted from David G. Sullivan, Computer Science E-22
# Modified by:     <your name>, <your e-mail address>
# Date modified:   <current date>
# 
1

     
#
# A class for storing information about a student.
#
class StudentRecord():
    def __init__(self, id, lastName, firstName):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
    
#
# A class for storing information about a student's
# grade on a particular assignment.
#
class GradeRecord():
    def __init__(self, studentID, assignment, grade):
        self.studentID = studentID
        self.assignment = assignment   # e.g., "PS 1" or "midterm"
        self.grade = grade
    
    ### add your instance variables here ###
    
# 
# A simple in-memory database of student and grade information.
# 
        
class GradeDatabase():
    ### complete the constructor below ###
    def __init__(self):
        self.gr = []
        self.sr = []
                     
    #
    # addStudent - add a record for the student with the specified information
    #
    def addStudent(self, id, last, first):
        sr=StudentRecord(id,last,first)
        self.sr.append(sr)
    ### complete the method below ###

    #
    # addGrade - add a record for the grade entry with the specified details
    #
    def addGrade(self, id, asst, grade):
        gr=GradeRecord(id,asst,grade)
        self.gr.append(gr)
    
    ### complete the method below ###
        
    # 
    # printStudents - print the entries in the student table
    #
    def printStudents(self):
        print()
        print("id\tlast\t\tfirst")
        print("--------------------------------------------");
        for s in self.sr:
            print(s.id, "\t", s.lastName, "\t\t", s.firstName)
        ### complete the method below ###
        
    
    # 
    # printGrades - print the entries in the grade table
    # 
    def printGrades(self):
        print()
        print("id\tassignment\tgrade")
        print("--------------------------------------------")
        for g in self.gr:
            print(g.studentID, "\t", g.assignment, "\t\t", g.grade)
        ### complete the method below ###

    
    # 
    # printStudentsGrades - print a "join" of the student and grade
    # tables.  See the problem set handout for more details.
    #
    def printStudentsGrades(self):
        print()
        print("last\t\tfirst\tassignment\tgrade")
        print("------------------------------------------------")
        for s in self.sr:
            for g in self.gr:
                if (s.id==g.studentID):
                    print(s.lastName, "\t\t", s.firstName, "\t", g.assignment, "\t", g.grade)
        ### complete the method below ###
        
    
def main():
        
        db = GradeDatabase()
        op = 0   
     
        while op != 6:
            print()
            print("(1) Add student")
            print("(2) Add grade")
            print("(3) Print students")
            print("(4) Print grades")
            print("(5) Print each student's grades")
            print("(6) Exit")
            op = eval(input("Which operation (1-6)? "))
            
            if op == 1:
                sid = input("    student id: ")
                last = input("    last: ")
                first = input("    first: ")
                db.addStudent(sid, last, first)
            elif op == 2:
                sid = input("    student id: ")
                asst = input("    assignment: ")
                grade = input("    grade: ")
                db.addGrade(sid, asst, grade)
            elif op == 3:
                db.printStudents()
            elif op == 4:
                db.printGrades()
            elif op == 5:
                db.printStudentsGrades();
            elif op != 6:
                print("Invalid choice. Please enter a number from 1-6.")
    
main()
