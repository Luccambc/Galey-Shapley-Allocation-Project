'''
Data Structures:
students = {"cod" : [[student project preferences in order], student qualification]}
projects = {"cod" : [number of available slots, required qualification, {students in project}]}
'''

projects = {}
availableStudents = {}
availableStudentsCodes = []
notAlocatedStudents = {}

def addProject(projectLine):
    removingParenthesis = projectLine[1:-1]
    # print(removingParenthesis)
    separatingInformation = removingParenthesis.split(", ")
    # print(separatingInformation)
    projectCode = separatingInformation[0]
    availableStudentsCodes.append(projectCode)
    slots, qualification = map(int, separatingInformation[1:3])
    projects[projectCode] = [slots, qualification, {}] 
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

"""
Testing the dataset read and manipulation to the defined data structures
print(projects)
print(availableStudents)
"""

print(projects['P30'])
print(availableStudents['P30'])

while len(availableStudentsCodes) != 0:
    # getting the first available and removing him from the data structures
    currentStudentCode = availableStudentsCodes[0]
    currentStudentData = availableStudents[currentStudentCode]
    availableStudentsCodes.remove(currentStudentCode)
    availableStudents.pop(currentStudentCode)
    '''
    Data Structures:
    students = {"cod" : [[student project preferences in order], student qualification]}
    projects = {"cod" : [number of available slots, required qualification, {students in project}]}
    '''
    studentAlocated = False
    for projectPreferenceCode in currentStudentData[0]:
        projectPreferenceData = projects[projectPreferenceCode]
        # Case in which the student has the qualification for it and there is a spot in the project
        if currentStudentData[1] >= projectPreferenceData[1] and projectPreferenceData[0] < len(projectPreferenceData[2]):
            projects[projectPreferenceCode][2][currentStudentCode] = currentStudentData
            studentAlocated = True
            break
        # If a student doesnt have the qualification he will not fill the spot no matter what
        # If there isnt a spot, I must fill the spot with the least qualified possible member to maximize the occupation of projects
        elif currentStudentData[1] >= projectPreferenceData[1] and projectPreferenceData[0] == len(projectPreferenceData[2]): 
            for studentCode, studentData in projectPreferenceData[2].items():
                # if the current student has worse qualifications than any of the members there must be a substitution and the removed member must be reinserted in the availableStudents to be considered for another opportunity
                if currentStudentData[1] < studentData[1]:
                    # making the substitution
                    projects[projectPreferenceCode][2].pop(studentCode)
                    projects[projectPreferenceCode][2][currentStudentCode] = studentData
                    # adding the removed student for other opportunities in projects
                    availableStudents[studentCode] = studentData
                    availableStudentsCodes.append(studentCode)
                    studentAlocated = True
                    break
            if studentAlocated:
                break
    if studentAlocated == False:
        notAlocatedStudents[currentStudentCode] = currentStudentData


    


