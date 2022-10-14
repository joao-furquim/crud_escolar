# Projeto de um Sistema Escolar


from typing import List, Literal
from pydantic import (BaseModel, constr, PositiveInt, ConstrainedFloat)
import os

# ------------------------Validações----------------------------

class TurmasValidator(BaseModel):
    creditos: PositiveInt()
    tempo: PositiveInt()
    codigo: constr(max_length=50, min_length=2)
    disciplina: Literal["portugues", "matematica", "ciencias"]


class PessoaValidator(BaseModel):
    nome: constr(max_length=50, min_length=2)
    sobrenome: constr(max_length=50, min_length=2)
    idade: PositiveInt()
    sexo: Literal["masculino", "feminino"]
    cpf: constr(max_length=11, min_length=11, regex="(\d){11}")
    raca: Literal["branca", "preta", "parda", "indigena", "amarela"]


class AlunoValidador(PessoaValidator):
    ano_inicio: PositiveInt()
    previsao_termino: PositiveInt()
    tempo_curso: ConstrainedFloat()
    disciplinas: List[str] = []


class ProfessorValidator(PessoaValidator):
    turmas: List[str] = []
    tempo_faculdade: ConstrainedFloat()

# ------------------------Pessoas----------------------------

class Pessoa:
    def __init__(self):
        self.nome: str
        self.sobrenome: str
        self.idade: int
        self.sexo: str
        self.identificacao: str
        self.raca: str


class Alunos(Pessoa):
    def __init__(self):
        self.ano_inicio: int
        self.previsao_termino: int
        self.tempo_curso: float
        self.disciplinas: List[str] = []

    def create_aluno(self, aluno: AlunoValidador):
        return aluno

    def disciplinas_matriculadas(self) -> str:
        return str(len(self.disciplinas))


class Professor(Pessoa):
    def __init__(self):
        self.turmas: List[str] = []
        self.tempo_faculdade: float

    def quantidade_de_turmar(self) -> str:
        return str(len(self.turmas))

    def create_prof(self, prof: ProfessorValidator):
        return prof

    @staticmethod
    def add_turma(prof, disciplina_):
        prof.turma.append(disciplina_)
        return prof


# ------------------------materias----------------------------

class Turmas():
    def __init__(self):
        self.codigo: str
        self.disciplina: str
        self.creditos: int
        self.tempo: int

    def create_turma(self, turma: TurmasValidator):
        return turma


#  Controle do codigo

if __name__ == '__main__':
    os.system('clear') or None

    # Variavel de controle do codigo
    ligado = True

    # Simulação de um banco de dados
    alunos = []
    professores = []
    turmas = []

    while (ligado):

        select_operation = input(
            "Selecione uma operação: \n "
            "1 - Listagem de Alunos; \n "
            "2 - Listagem de Professores; \n "
            "3 - Listagem de Turmas; \n "
            "4 - Cadastro de professores; \n "
            "5 - Cadastro de alunos; \n "
            "6 - Cadastro de turmas; \n "
            "7 - excluir aluno; \n"
            "8 - excluir professor \n"
            "9 - adicionar materia do aluno; \n"
            "10 - remover materia do aluno; \n"
            "11 - adicionar turma ao professor; \n"
            "12 - remover turma ao professor; \n"
            "13 - finalizar programa; \n"
            "14 - mock de dados. \n"
            "Operação: ")


        if select_operation == "1":
            os.system('clear') or None
            print("Alunos: ", alunos, "\n")

        elif select_operation == "2":
            os.system('clear') or None
            print("Professores: ", professores, "\n")

        elif select_operation == "3":
            os.system('clear') or None
            print("Turmas: ", turmas, "\n")

        elif select_operation == "4":
            os.system('clear') or None

            nome = input("Nome: ")
            sobrenome = input("sobrenome: ")
            idade = input("idade: ")
            sexo = input("sexo: ")
            cpf = input("cpf: ")
            raca = input("raca: ")
            turmas_i = input("turmas: ")
            tempo_faculdade = input("Tempo de Faculdade: ")

            dados = {
                "nome": nome,
                "sobrenome": sobrenome,
                "idade": idade,
                "sexo": sexo,
                "cpf": cpf,
                "raca": raca,
                "turmas": [turmas_i],
                "tempo_faculdade": tempo_faculdade
            }

            professor_ = ProfessorValidator(**dados)
            prof = Professor()
            prof_ = prof.create_prof(prof=professor_)
            professores.append(prof_)
            print("Professores: ", professores, "\n")


        elif select_operation == "5":
            os.system('clear') or None

            nome = input("Nome: ")
            sobrenome = input("sobrenome: ")
            idade = input("idade: ")
            sexo = input("sexo: ")
            cpf = input("cpf: ")
            raca = input("raca: ")
            ano_inicio = input("ano_inicio: ")
            previsao_termino = input("previsao_termino: ")
            tempo_curso = input("tempo_curso: ")
            disciplinas = input("disciplinas: ")

            dados = {
                "nome": nome,
                "sobrenome": sobrenome,
                "idade": idade,
                "sexo": sexo,
                "cpf": cpf,
                "raca": raca,
                "ano_inicio": ano_inicio,
                "previsao_termino": previsao_termino,
                "tempo_curso": tempo_curso,
                "disciplinas": [disciplinas]
            }

            aluno1_ = AlunoValidador(**dados)
            al = Alunos()

            teste1 = al.create_aluno(aluno=aluno1_)
            alunos.append(teste1)
            print("Alunos: ", alunos, "\n")

        elif select_operation == "6":
            os.system('clear') or None

            codigo = input("codigo: ")
            disciplina = input("disciplina: ")
            creditos = input("creditos: ")
            tempo = input("tempo: ")

            dados = {
                "codigo": codigo,
                "disciplina": disciplina,
                "creditos": creditos,
                "tempo": tempo
            }

            turma_validate = TurmasValidator(**dados)
            turma = Turmas()
            turma_ = turma.create_turma(turma=turma_validate)
            turmas.append(turma_)
            print("Turmas: ", turmas, "\n")

        elif select_operation == "7":
            os.system('clear') or None

            cpf = input("CPF: ")

            idx = -1
            for i in alunos:
                idx = idx + 1
                if cpf == i.cpf:
                    alunos.remove(idx)


        elif select_operation == "8":
            os.system('clear') or None
            print("Programa finalizado !")
            cpf = input("CPF: ")

            idx = -1
            for i in professores:
                idx = idx + 1
                if cpf == i.cpf:
                    professores.remove(i)

        elif select_operation == "9":
            os.system('clear') or None

            cpf = input("CPF: ")
            codigo = input("Disciplina: ")

            for i in alunos and codigo in turmas:
                if cpf == i.cpf:
                    i.disciplinas.append(codigo)


        elif select_operation == "10":
            os.system('clear') or None

            cpf = input("CPF: ")
            codigo = input("Disciplina: ")

            for i in alunos and codigo in turmas:
                if cpf == i.cpf:
                    i.disciplinas.remove(codigo)

        elif select_operation == "11":
            os.system('clear') or None

            cpf = input("CPF: ")
            codigo = input("Disciplina: ")

            for i in professores and codigo in turmas:
                if cpf == i.cpf:
                    i.turmas.append(codigo)


        elif select_operation == "12":
            os.system('clear') or None

            cpf = input("CPF: ")
            codigo = input("Disciplina: ")

            for i in professores:
                if cpf == i.cpf and codigo in turmas:
                    i.turmas.remove(codigo)

        elif select_operation == "13":
            os.system('clear') or None
            print("Programa finalizado ! \n")
            ligado = False

        elif select_operation == "14":
            os.system('clear') or None
            alunos_ = [{
                "nome": "joao",
                "sobrenome": "123",
                "idade": 20,
                "sexo": "masculino",
                "cpf": "11111111111",
                "raca": "parda",
                "ano_inicio": 2018,
                "previsao_termino": 2023,
                "tempo_curso": 4,
                "disciplinas": []
            },
            {
                "nome": "pedro",
                "sobrenome": "123",
                "idade": 20,
                "sexo": "masculino",
                "cpf": "22222222222",
                "raca": "parda",
                "ano_inicio": 2018,
                "previsao_termino": 2023,
                "tempo_curso": 4,
                "disciplinas": []
            }
            ]
            for i in alunos_:

                aluno1_ = AlunoValidador(**i)
                al = Alunos()

                teste1 = al.create_aluno(aluno=aluno1_)
                alunos.append(teste1)

            professores_ = [{
                "nome": "evaldo",
                "sobrenome": "patrik",
                "idade": 26,
                "sexo": "masculino",
                "cpf": "33333333333",
                "raca": "amarela",
                "turmas": [],
                "tempo_faculdade": 8
            },
            {
                "nome": "Norton",
                "sobrenome": "liaz",
                "idade": 22,
                "sexo": "masculino",
                "cpf": "44444444444",
                "raca": "indigena",
                "turmas": [],
                "tempo_faculdade": 5
            }
            ]
            for i in professores_:
                professor_ = ProfessorValidator(**i)
                pro = Professor()

                teste = pro.create_prof(prof=professor_)
                professores.append(teste)

            Turmas_ = [{
                "creditos": 10,
                "tempo": 60,
                "codigo": "teste123",
                "disciplina": "matematica",

            },
            {
                "creditos": 10,
                "tempo": 60,
                "codigo": "teste456",
                "disciplina": "portugues",
            }
            ]
            for i in Turmas_:
                turma_ = TurmasValidator(**i)
                tur = Turmas()

                teste = tur.create_turma(turma=turma_)
                turmas.append(teste)

            print("Professores: ", professores, "\n")
            print("Alunos: ", alunos, "\n")
            print("Turmas: ", turmas, "\n")

        else:
            os.system('clear') or None
            print("Messagem: comando não reconhecido \n")