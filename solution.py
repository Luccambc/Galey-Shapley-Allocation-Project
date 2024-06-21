'''
Data Structures:
students = {"cod" : [[student project preferences in order], student qualification]}
projects = {"cod" : [number of available slots, required qualification]}
'''

def addProject(projectLine):
    removingParenthesis = projectLine[1:len(projectLine) - 1]
    # print(removingParenthesis)
    separatingInformation = removingParenthesis.split(", ")
    # print(separatingInformation)
    projects[separatingInformation[0]] = list(map(int, separatingInformation[1:3]))
    # print(projects)

def addStudent(studentLine):
    provCode1, projectInformation = studentLine.split(":")
    # print(provCode1)
    # print(projectInformation)
    provCode2 = provCode1.replace("(", "")
    studentCode = provCode2.replace(")", "")
    # print(studentCode)
    separatingInformation = projectInformation.split(") (")
    # print(separatingInformation)
    studentPreferences = (separatingInformation[0].replace("(", "")).split(", ")
    # print(studentPreferences)
    studentQualification = int(separatingInformation[1].replace(")", ""))
    # print(studentQualification)
    availableStudents[studentCode] = [studentPreferences, studentQualification]
    print(availableStudents)

projects = {}
availableStudents = {}
notAlocatedStudents = {}

"""
Testing the addDataStructure for some cases:
addProject("(P1, 3, 5)")
addStudent("(A1):(P1, P30, P50) (5)")
addStudent("(A198):(P2, P50) (3)")
"""

