'''
Para resolver o problema em questão e buscar um emparelhamento máximo e estável dado um grafo bipartido, foram usadas as seguintes estruturas de dados como exemplo para dois projetos e três alunos: 

students = {
    'A1': [['P1', 'P30', 'P50'], 5], 
    'A2': [['P1', 'P30', 'P51'], 5], 
    'A3': [['P30', 'P34', 'P35'], 3]
}

projects = {
    'P1': [3, 5, {'A1': [['P1', 'P30', 'P50'], 5], 'A2': [['P1', 'P30', 'P51'], 5]}], 
    'P2': [1, 5, {'A32': [['P2', 'P20', 'P4'], 5]}], 
}
'''

# Inicializando as variáveis necessárias para realizar o controle e alocação de estudantes em seus projetos. 
projects = {}
students = {}
availableStudentsCodes = []
notAlocatedStudents = {}

# Lê linhas de projeto e adiciona, no modelo definido, os projetos
def addProject(projectLine):
    removingParenthesis = projectLine[1:-1]
    separatingInformation = removingParenthesis.split(", ")
    projectCode = separatingInformation[0]
    slots, qualification = map(int, separatingInformation[1:3])
    projects[projectCode] = [slots, qualification, {}] 

# Lê linhas de aluno e adiciona, no modelo definido, os alunos
def addStudent(studentLine):
    provCode1, projectInformation = studentLine.split(":")
    provCode2 = provCode1.replace("(", "")
    studentCode = provCode2.replace(")", "")
    availableStudentsCodes.append(studentCode)
    if studentCode == 'A177':
        separatingInformation = projectInformation.split(")(")
    else:
        separatingInformation = projectInformation.split(") (")
    studentPreferences = (separatingInformation[0].replace("(", "")).split(", ")
    studentQualification = int(separatingInformation[1].replace(")", ""))
    students[studentCode] = [studentPreferences, studentQualification]

# Recebe o nome do arquivo e chama as funções necessárias de leitura por um filtro por caractéres
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

# Função para mostrar os alunos alocados em cada ums dos projetos
def extract_keys(data, key):
    if key in data:
        sub_dict = data[key][2]
        return list(sub_dict.keys())
    return []

# Realiza chamada de função de leitura de arquivos para o dataEntry.txt
processFile('dataEntry.txt')

contador = 1
while len(availableStudentsCodes) != 0: # or contador == 100:
    # A cada iteração, iremos remover o primeiro aluno das lista dos disponíveis e verificar suas preferências
    currentStudentCode = availableStudentsCodes[0]
    print(f"Iteracao {contador}")
    print(f'Aluno {currentStudentCode} em analise...')
    currentStudentData = students[currentStudentCode]
    availableStudentsCodes.remove(currentStudentCode)
    # Variável que faz o controle do aluno ter sido alocado para algum projeto, ou não
    currentStudentAllocated = False

    currentStudentProjectPreferences = currentStudentData[0]
    currentStudentGrade = currentStudentData[1]
    for projectPreferenceCode in currentStudentProjectPreferences:
        print(f'Aluno {currentStudentCode} aplicando para {projectPreferenceCode}')
        projectPreferenceData = projects[projectPreferenceCode]

        projectPreferenceSlots = projectPreferenceData[0]   
        projectPreferenceMinGrade = projectPreferenceData[1]
        projectPreferenceStudents = projectPreferenceData[2]

        # Caso o aluno não tenha a nota necessário ele não será alocado 
        # Caso o aluno tenha a nota necessário e exista uma vaga disponível no projeto, ele será alocado
        if currentStudentGrade >= projectPreferenceMinGrade and projectPreferenceSlots > len(projectPreferenceStudents): 
            print(f'Aluno {currentStudentCode} esta qualificado e foi alocado em {projectPreferenceCode} com sucesso!\n')
            # Insere o aluno nos alunos alocados naquele projeto de preferência
            projects[projectPreferenceCode][2][currentStudentCode] = currentStudentData
            currentStudentAllocated = True
            break

        # Caso não haja uma vaga, o algoritmo de Gale Shapley exige que o com a maior preferência seja alocado
        # Para maximizar a quantidade de alunos alocados, em caso de empate de preferência alocamos aquele aluno com a menor nota necessário para fazer parte do projeto visto que o com a maior nota pode ter escolhas maiores
        elif currentStudentGrade >= projectPreferenceMinGrade and projectPreferenceSlots == len(projectPreferenceStudents):
            # Atraves deste loop iremos verificar os alunos alocados para o projeto de preferência do aluno atual
            for studentCode, studentData in projectPreferenceStudents.items():
                studentProjectPreferences = studentData[0]
                studentGrade = studentData[1]

                # Se estudante atual tiver uma preferência maior pelo projeto, haverá uma substituição
                if currentStudentProjectPreferences.index(projectPreferenceCode) < studentProjectPreferences.index(projectPreferenceCode):
                    print(f'{currentStudentCode} ou {studentCode}. Quem tem a maior preferencia pelo projeto {projectPreferenceCode}?')
                    # Substuição do atual pelo que está sendo analisado
                    projects[projectPreferenceCode][2].pop(studentCode)
                    projects[projectPreferenceCode][2][currentStudentCode] = currentStudentData
                    # Adiciona o aluno que tinha menor preferência por aquele projeto para ser novamente considerado para outros
                    students[studentCode] = studentData
                    availableStudentsCodes.append(studentCode)
                    print(f'{currentStudentCode} substituira o aluno {studentCode}, o qual tem menor preferência.')
                    currentStudentAllocated = True
                    break

                # Se os estudantes tiverem preferência igual para o projeto faz sentido para maximizar os alunos alocados você tirar o com a maior qualificação, pois ele terá oportunidade de ser alocado em mais projetos
                elif currentStudentProjectPreferences.index(projectPreferenceCode) == studentProjectPreferences.index(projectPreferenceCode):
                    print(f'{currentStudentCode} ou {studentCode}. Quem e o menos qualificado?')
                    if currentStudentGrade < studentGrade:
                        print(f'{currentStudentCode} substituira o aluno {studentCode}, o qual e menos qualificado.')
                        # Substuição do atual pelo que está sendo analisado
                        projects[projectPreferenceCode][2].pop(studentCode)
                        projects[projectPreferenceCode][2][currentStudentCode] = currentStudentData
                        # Adiciona o aluno que tinha menor preferência por aquele projeto para ser novamente considerado para outros
                        students[studentCode] = studentData
                        availableStudentsCodes.append(studentCode)
                        currentStudentAllocated = True
                        break
                    else:
                        print(f'{studentCode} mais qualificado que {currentStudentCode}, portanto ele fica no projeto.')
 
            if currentStudentAllocated:
                break
        
    if currentStudentAllocated == False:
        print(f'Aluno {currentStudentCode} nao pode ser alocado em nenhum projeto de sua preferencia.\n')
        notAlocatedStudents[currentStudentCode] = currentStudentData
    contador += 1

#print(len(notAlocatedStudents))
# print(projects)
alocatedStudents = 0
for key, value in projects.items():
    alocatedStudents += len(value[2])
print(f"Em {contador} iteracoes foram alocados {alocatedStudents} alunos dos {len(students)} disponiveis.")


projectAllocation = {key: extract_keys(projects, key) for key in projects.keys()}
print(projectAllocation)


