'''
Why did I create this program?

- This program is used when midterms or finals examination is close. This program's objective is to help the student 
review the lectures that has been tackled throughout the certain term.
'''
import datetime as dt

student = ""
studentNumber = ""
sectionAndYear = ""
currentDate = dt.datetime.now()
units = []
subject = []

print("============STUDENT_PROFILE================")
print("Name:",student)
print("Student#:",studentNumber)
print("Section/Year:",sectionAndYear)
print("Date:",currentDate)
print("================UNITS======================")
for unit in units:
    print(unit)
print("===========================================")
unitChosen = int(input("Which of the units would you like to review? (1-total number of units)\n"))   
if unitChosen == 1:
    print("===============LECTURE=====================")
    for lecture in subject:
        print(lecture)
exit()
