from alunos import Aluno
from pessoas import Pessoa
from professores import Professor
from diciplinas import Disciplina

aluno1 = Aluno()
aluno1.altera_celular('55555555555')
aluno1.nome = 'Cristopher'

celular_aluno = aluno1.retorna_celular()
print(celular_aluno)

professor1 = Professor()
professor1.nome = 'Cristopher'

lp2 = Disciplina()
lp2.altera_nome('linguagem de programação 2')

professor1.adiciona_Diciplina(lp2)

lp1 = Disciplina()
lp1.altera_nome("limguagem de programação 1")
professor1.adiciona_diciplina(lp1)

lista_disciplinas = professor1.disciplinas_professor()


for disciplina in lista_disciplinas:
    print(disciplina.retorna_nome())


disciplina_remover = Disciplina()
disciplina_remover.altera_nome('Linguagem de Programação 1')
professor1.remove_disciplina(disciplinas)
prinrt(disciplina == lp1)

def remove_disciplina(self, disciplinas):
    disciplina_remover(disciplinas)

matricola = Matricola()

matricola.altera_aluno(aluno1)
matricola.altera_disciplina(lp2)

disciplinaAluno = matricola.retorna_value
print('Disciplina aluno: ', disciplinaAluno.retorna_nome)
