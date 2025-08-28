contas = []

taxadepositar = 1.00
taxasacar = 2.50
taxatransferir = 5.00

def criar_conta():
    nome = input("Insira seu nome: ")
    numero = input("Insira o número da conta: ")
    senha = input("Crie sua senha: ")
    saldo = float(input("Insira o saldo inicial: R$ "))
    for conta in contas:
        if conta[1] == numero:
            print("Esta conta já existe.")
            return
    contas.append([nome, numero, senha, saldo])
    print("Sua conta foi cadastrada com sucesso!")

def autenticar(numero, senha):
    for conta in contas:
        if conta[1] == numero and conta[2] == senha:
            return conta
    return None

def sacar(conta):
    valor = float(input("Insira o valor do saque: R$ "))
    total = valor + taxasacar
    if conta[3] >= total:
        conta[3] -= total
        print("O Saque de R$", valor, "foi realizado. Taxa cobrada: R$", taxasacar)
    else:
        print("Saldo insuficiente.")

def depositar(conta):
    valor = float(input("Insira o valor do depósito: R$ "))
    total = valor - taxadepositar
    if total > 0:
        conta[3] += total
        print("O depósito de R$", valor, "foi realizado. Taxa cobrada: R$", taxadepositar)
    else:
        print("O valor do depósito é insuficiente para cobrir a taxa.")

def transferir(conta_origem):
    destino_numero = input("Insira o número da conta de destino: ")
    valor = float(input("Insira o valor da transferência: R$ "))
    total = valor + taxatransferir
    if conta_origem[3] < total:
        print("Saldo insuficiente para transferência.")
        return
    conta_destino = None
    for conta in contas:
        if conta[1] == destino_numero:
            conta_destino = conta
            break
    if conta_destino:
        conta_origem[3] -= total
        conta_destino[3] += valor
        print("A transferência de R$", valor, "foi realizada com sucesso. Taxa cobrada: R$", taxatransferir)
    else:
        print("A conta de destino não existe")

def listar_saldo(conta):
    print("Nome do cliente:", conta[0], "| Saldo: R$", conta[3])

def menu_cliente(conta):
    while True:
        print("BANCO SITACOB")
        print("1 -- Sacar --")
        print("2 -- Depositar --")
        print("3 -- Transferir --")
        print("4 -- Ver saldo --")
        print("5 -- Sair --")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            sacar(conta)
        elif opcao == "2":
            depositar(conta)
        elif opcao == "3":
            transferir(conta)
        elif opcao == "4":
            listar_saldo(conta)
        elif opcao == "5":
            print("Saindo da conta...")
            break
        else:
            print("Opção inválida.")

def login():
    numero = input("Insira o número da sua conta: ")
    senha = input("Insira a senha da sua conta: ")
    conta = autenticar(numero, senha)
    if conta:
        print("Seja bem-vindo,", conta[0], "!")
        menu_cliente(conta)
    else:
        print("O login falhou. Número ou senha incorretos.")

def menu():
    while True:
        print("BANCO SITACOB")
        print("1 -- Cadastrar nova conta --")
        print("2 -- Fazer login --")
        print("3 -- Sair --")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Encerrando o sistema bancário...")
            break
        else:
            print("Opção inválida.")

menu()