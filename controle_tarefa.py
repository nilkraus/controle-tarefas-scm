tarefas = []

def cadastrar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append(descricao)
    print("Tarefa cadastrada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nTarefas cadastradas:")
        for numero, tarefa in enumerate(tarefas, start=1):
            print(f"{numero}. {tarefa}")

while True:
    print("\n=== CONTROLE DE TAREFAS ===")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")