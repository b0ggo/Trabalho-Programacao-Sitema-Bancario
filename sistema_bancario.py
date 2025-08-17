contas = []

TAXA_SAQUE = 2.50
TAXA_DEPOSITO = 1.00
TAXA_TRANSFERENCIA = 5.00

def criar_conta():
    nome = input("Nome do cliente: ")
    numero = input("Número da conta: ")
    senha = input("Crie uma senha: ")
    saldo = float(input("Saldo inicial: R$ "))
    for conta in contas:
        if conta[1] == numero:
            print("Conta já existe.")
            return
    contas.append([nome, numero, senha, saldo])
    print("Conta cadastrada com sucesso!")

def autenticar(numero, senha):
    for conta in contas:
        if conta[1] == numero and conta[2] == senha:
            return conta
    return None

def sacar(conta):
    valor = float(input("Valor do saque: R$ "))
    total = valor + TAXA_SAQUE
    if conta[3] >= total:
        conta[3] -= total
        print("Saque de R$", valor, "realizado. Taxa: R$", TAXA_SAQUE)
    else:
        print("Saldo insuficiente.")

def depositar(conta):
    valor = float(input("Valor do depósito: R$ "))
    total = valor - TAXA_DEPOSITO
    if total > 0:
        conta[3] += total
        print("Depósito de R$", valor, "realizado. Taxa: R$", TAXA_DEPOSITO)
    else:
        print("Valor do depósito insuficiente para cobrir a taxa.")

def transferir(conta_origem):
    destino_numero = input("Número da conta de destino: ")
    valor = float(input("Valor da transferência: R$ "))
    total = valor + TAXA_TRANSFERENCIA
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
        print("Transferência de R$", valor, "realizada com sucesso. Taxa: R$", TAXA_TRANSFERENCIA)
    else:
        print("Conta de destino não encontrada.")

def listar_saldo(conta):
    print("Cliente:", conta[0], "| Saldo: R$", conta[3])

def menu_cliente(conta):
    while True:
        print("MENU")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Transferir")
        print("4. Ver saldo")
        print("5. Sair")
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
    numero = input("Número da conta: ")
    senha = input("Senha: ")
    conta = autenticar(numero, senha)
    if conta:
        print("Bem-vindo,", conta[0], "!")
        menu_cliente(conta)
    else:
        print("Login falhou. Número ou senha incorretos.")

def menu():
    while True:
        print("BANCO")
        print("1. Cadastrar nova conta")
        print("2. Fazer login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Encerrando o sistema. Obrigado!")
            break
        else:
            print("Opção inválida.")

menu()