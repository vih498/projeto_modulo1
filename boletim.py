lista_alunos = []

#Calcular média de notas e situação
def calcular_media_situacao(n1, n2):
    media = (n1 + n2) / 2
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 4:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return media, situacao

#Cadastrar alunos
def cadastrar():
    print('\n---- Cadastrar Estudante ----')
    matricula = input("Matrícula: ").strip()
    nome = input("Nome: ").strip()

    #Validação se matrícula já existe
    for aluno in lista_alunos:
        if aluno['matricula'] == matricula:
            print("Matrícula já cadastrada.")
            return

    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            raise ValueError
    except ValueError:
        print("As notas devem estar entre 0 e 10.")
        return

    media, situacao = calcular_media_situacao(nota1, nota2)

    aluno = {
        'matricula': matricula,
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2,
        'media': media,
        'situacao': situacao
    }

    lista_alunos.append(aluno)
    print("Estudante cadastrado com sucesso.")

#Alterar dados de aluno
def alterar():
    print('\n---- Alterar Estudante ----')
    matricula = input("Digite a matrícula do aluno: ").strip()

    for aluno in lista_alunos:
        if aluno['matricula'] == matricula:
            print(f"Alterando dados do aluno: {aluno['nome']}")
            nome = input("Novo nome (ou Enter para manter): ").strip()
            if nome:
                aluno['nome'] = nome

            try:
                nota1 = input("Nova nota 1 (ou Enter para manter): ").strip()
                nota2 = input("Nova nota 2 (ou Enter para manter): ").strip()

                if nota1:
                    aluno['nota1'] = float(nota1)
                if nota2:
                    aluno['nota2'] = float(nota2)

                aluno['media'], aluno['situacao'] = calcular_media_situacao(aluno['nota1'], aluno['nota2'])
                print("Dados atualizados com sucesso.")
            except ValueError:
                print("Notas inválidas.")
            return

    print("Matrícula não encontrada.")

#Excluir aluno
def excluir():
    print('\n---- Excluir Estudante ----')
    matricula = input("Digite a matrícula do aluno: ").strip()

    for i, aluno in enumerate(lista_alunos):
        if aluno['matricula'] == matricula:
            confirmacao = input(f"Tem certeza que deseja excluir o aluno {aluno['nome']}? (s/n): ").strip().lower()
            if confirmacao == 's':
                lista_alunos.pop(i)
                print("Aluno excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
            return

    print("Matrícula não encontrada.")

#Mostrar em lista todos os alunos
def listar():
    print('\n---- Relatório dos Estudantes ----')
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return

    print(f"{'Matrícula':<12}{'Nome':<20}{'Nota1':<7}{'Nota2':<7}{'Média':<7}{'Situação'}")
    print("-" * 60)
    for aluno in lista_alunos:
        print(f"{aluno['matricula']:<12}{aluno['nome']:<20}{aluno['nota1']:<7.1f}{aluno['nota2']:<7.1f}{aluno['media']:<7.1f}{aluno['situacao']}")
    print("-" * 60)

#Menu principal
while True:
    print('\n=== Boletim EduSimples ===')
    print('1 - Cadastrar')
    print('2 - Alterar')
    print('3 - Excluir')
    print('4 - Listar')
    print('5 - Sair do Sistema')

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Opção inválida. Digite um número de 1 a 5.')
        continue

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        alterar()
    elif opcao == 3:
        excluir()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        print('Sistema finalizado com sucesso!')
        break
    else:
        print('Opção inválida.')