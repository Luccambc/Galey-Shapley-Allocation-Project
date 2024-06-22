# Gale Shapley Algorithm for Student Allocation

Este projeto é uma implementação do Gale Shapley algorithm cujo propósito é buscar um emparelhamento máximo e estável dado um grafo bipartido. 

Para formar o grafo bipartido, foi usado uma base de dados em formato txt que possui alunos e projetos. Ambos possuem algumas informações importantes para o máximo de alunos serem alocados em suas preferências de projeto. 

A implementação, portanto, inicia consumindo o arquivo txt e fomentando as seguintes estruturas definidas que serão utilizada para resolver o problema em questão. 

Os alunos possuem seus códigos, suas preferências de projetos e suas nota. Por isso, foi utilizado um dicionário que contém como chave dos alunos seus código e suas outras informações relavantes como valor correspondente. Para três alunos, tal estrutura pode ser observada abaixo:
 
```python
availableStudents = {
    'A1': [['P1', 'P30', 'P50'], 5], 
    'A2': [['P1', 'P30', 'P51'], 5], 
    'A3': [['P30', 'P34', 'P35'], 3]
}
```

Os projeto terão uma estrutura similar, possuem seus códigos, o número de vagas disponíveis e o requisito mínimo de nota. Além disso, para termos um controle dos alunos presentes naquele projeto, adicionamos um dicionário que tem os alunos alocados ao projeto. Para dois projetos, tal estrutura pode ser observada abaixo:
 
```python
projects = {
    'P1': [3, 5, {'A1': [['P1', 'P30', 'P50'], 5], 'A2': [['P1', 'P30', 'P51'], 5]}], 
    'P2': [1, 5, {'A32': [['P2', 'P20', 'P4'], 5]}], 
}
```

Para ler o arquivo e adequar os dados às estruturas pensadas foram usadas as seguintes funções:

1. A função abaixo "addProject", lê a linha dos projetos e remove caractéres irrelevantes e converte alguns dados para seus devidos tipos. 

![imagem de leitura de projeto](./images/addProject.png)

2. A função "addStudent", lê a linha dos alunos e remove caractéres irrelevantes e converte alguns dados para seus devidos tipos. 

![imagem de leitura de projeto](./images/addStudent.png)

3. Por fim, a função "processFile", abre o arquivo "dataEntry.txt" e realiza a leitura e chamada das funções anteriores para compor os dicionários definidos com as informações necessárias. 

![imagem de leitura de projeto](./images/processFile.png)




