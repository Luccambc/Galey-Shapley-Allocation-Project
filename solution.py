'''
Data Structures:
students = {"cod" : [[student project preferences in order], student qualification]}
projects = {"cod" : [number of available slots, required qualification, [students in project]]}
'''

projects = {}
availableStudents = {}
notAlocatedStudents = {}

def addProject(projectLine):
    removingParenthesis = projectLine[1:-1]
    # print(removingParenthesis)
    separatingInformation = removingParenthesis.split(", ")
    # print(separatingInformation)
    projectCode = separatingInformation[0]
    slots, qualification = map(int, separatingInformation[1:3])
    projects[projectCode] = [slots, qualification, []] 
    # print(projects)

def addStudent(studentLine):
    provCode1, projectInformation = studentLine.split(":")
    # print(provCode1)
    # print(projectInformation)
    provCode2 = provCode1.replace("(", "")
    studentCode = provCode2.replace(")", "")
    # print(studentCode)
    if studentCode == 'A177':
        separatingInformation = projectInformation.split(")(")
    else:
        separatingInformation = projectInformation.split(") (")
    # print(separatingInformation)
    studentPreferences = (separatingInformation[0].replace("(", "")).split(", ")
    # print(studentPreferences)
    studentQualification = int(separatingInformation[1].replace(")", ""))
    # print(studentQualification)
    availableStudents[studentCode] = [studentPreferences, studentQualification]
    # print(availableStudents)


def processFile(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            if "A" in line:
                print(availableStudents)
                addStudent(line)
            elif "P" in line:
                addProject(line)

"""
Testing the addDataStructure for some cases:
addProject("(P1, 3, 5)")
addStudent("(A1):(P1, P30, P50) (5)")
addStudent("(A198):(P2, P50) (3)")
"""

processFile('dataEntry.txt')

print(projects)
print(availableStudents)



