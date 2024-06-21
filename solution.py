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
    availableStudentsCodes.append(studentCode)
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

contador = 1
# len(availableStudentsCodes) != 0
while contador < 56:
    # getting the first available and removing him from the data structures
    currentStudentCode = availableStudentsCodes[0]
    print(f"Iteracao {contador}")
    print(f'Aluno {currentStudentCode} em analise...')
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
        print(f'Aluno {currentStudentCode} aplicando para {projectPreferenceCode}')
        projectPreferenceData = projects[projectPreferenceCode]
        # print(projectPreferenceData)
        # Case in which the student has the qualification for it and there is a spot in the project
        if currentStudentData[1] >= projectPreferenceData[1] and projectPreferenceData[0] > len(projectPreferenceData[2]): 
            print(f'Aluno {currentStudentCode} esta qualificado e foi alocado em {projectPreferenceCode} com sucesso!\n')
            projects[projectPreferenceCode][2][currentStudentCode] = currentStudentData
            studentAlocated = True
            break
        # If a student doesnt have the qualification he will not fill the spot no matter what
        # If there isnt a spot, I must fill the spot with the least qualified possible member to maximize the occupation of projects
        elif currentStudentData[1] >= projectPreferenceData[1] and projectPreferenceData[0] == len(projectPreferenceData[2]): 
            for studentCode, studentData in projectPreferenceData[2].items():
                print(f'{currentStudentCode} ou {studentCode}. Quem e o menos qualificado?')
                # if the current student has worse qualifications than any of the members there must be a substitution and the removed member must be reinserted in the availableStudents to be considered for another opportunity
                if currentStudentData[1] < studentData[1]:
                    print(f'{currentStudentCode} substituira o aluno {studentCode}, o qual e menos qualificado. ')
                    # making the substitution
                    projects[projectPreferenceCode][2].pop(studentCode)
                    projects[projectPreferenceCode][2][currentStudentCode] = studentData
                    # adding the removed student for other opportunities in projects
                    availableStudents[studentCode] = studentData
                    availableStudentsCodes.append(studentCode)
                    studentAlocated = True
                    break
                else:
                    print(f'{studentCode} mais qualificado que {currentStudentCode}.')
            if studentAlocated:
                break
        
    if studentAlocated == False:
        print(f'Aluno {currentStudentCode} nao pode ser alocado em nenhum projeto de sua preferencia.\n')
        notAlocatedStudents[currentStudentCode] = currentStudentData
    contador += 1

    
    # For A9, the student canot go to any of his choices of projects (change contador to 9)
"""    if contador == 100:
        break
    else:
        contador += 1"""

#print(len(notAlocatedStudents))
#print(projects)
alocatedStudents = 0
for key, value in projects.items():
    #print(f'Projeto {key} com {len(value[2])} alunos alocados')
    alocatedStudents += len(value[2])
print(f"Em {contador} iteracoes foram alocados {alocatedStudents} alunos dos {len(availableStudents)} disponiveis.")

# Função para mostrar os alunos alocados em cada ums dos 55 projetos
def extract_keys(data, key):
    if key in data:
        sub_dict = data[key][2]
        return list(sub_dict.keys())
    return []

projectAllocation = {key: extract_keys(projects, key) for key in projects.keys()}
print(projectAllocation)
