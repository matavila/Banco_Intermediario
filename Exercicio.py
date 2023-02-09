def Menu():
    #Variáveis Globais
    Clientes = {}
    LIMITE = 500
    Extrato =""
    Saque = 0
    Numero_saques = 0
    LIMITE_SAQUES = 3
    Saldo = 0
    menu = """


        <-----------------MENU--------------------->

        [0] = Depositar
        [1] = Sacar
        [2] = Extrato
        [3] = Cadastrar Novo Usuário
        [4] = Sair
        [5] = Clientes

        <------------------------------------------>

    """  
    print(menu)

    while True:
        opcao = int(input("DIGITE SUA OPÇÃO:  "))

        if opcao == 0:
            print("<------------Depositar------------->")
            Entrada = float(input("Digite o valor a ser depositado:  "))
            Saldo, Extrato = Depositar(Saldo, Entrada, Extrato)
            print(f"Seu saldo é : {Saldo:0.2f}")
            print()

        elif opcao == 1:
            print("<------------Sacar------------->")
            Saque, Extrato, Numero_saques = Sacar(Saldo,Saque, Extrato, LIMITE, Numero_saques, LIMITE_SAQUES)
            Saldo-= Saque
            print()
            print(f"O seu saldo é de {Saldo}")
            print("<------------Saque com Sucesso------------->")
            print()

        elif opcao == 2:
            print("=====================Extrato====================")
            Extrato = Retirar_Extrato(Extrato)
            print(f'\n Saldo: R${Saldo:0.2f}')
            print("================================================")

        elif opcao == 3:
            print("<------------Cadastrar------------->")
            Cliente = Cadastrar(Clientes)
            Clientes.update(Cliente)
            print("<------------Cadastro com Sucesso------------->")
            print()

        elif opcao == 4:
            print("Sair")
            break

        elif opcao == 5:
            BancoDados(Clientes)

        else:
            print("<------------ERRO------------->")
            Menu()


def Cadastrar(Clientes):
    Login = input("Digite o seu Login: ")
    if Login in Clientes:
        print("<------------CONTA JA EXISTENTE------------->")
        return

    Nome =input("Digite o seu nome: ")
    Data = input("Digite sua data de nascimento: ")
    Cpf = int(input("Digite seu cpf: "))
    Endereco = input("Digite seu Endereco: ")

    Novo = {f"{Login}": {"Nome":f"{Nome}", "Nascimento":f"{Data}","CPF":f"{Cpf}","Endereco":f"{Endereco}"}}
    return Novo


def Depositar(Saldo, Entrada, Extrato):
    if Entrada < 0:
        print("Operação inválida!! Valor de entrada negativo")

    else:
        print(f"Operação aceita!! O valor R${Entrada:0.2f} irá ser depositado")
        Saldo += Entrada
        Extrato += f"\nEntrada:   R${Entrada:0.2f}"

        return Saldo,Extrato
     
def BancoDados(Clientes):
    for chaves in Clientes.items():
        print(chaves)

def Sacar(Saldo, Saque , Extrato, LIMITE, Numero_saques, LIMITE_SAQUES):
    Saque = float(input("Digite o valor a ser sacado:  "))
    if Saque > Saldo:
        print("Operação inválida!! Valor sacado ultrapassa seu Saldo")

    elif Saque > LIMITE:
        print("Operação inválida!! Valor sacado ultrapassa seu limite")
            

    elif Saque < 0:
        print("Operação inválida!! Valor a sacar é negativo")
           

    else:
        Numero_saques+=1
        if Numero_saques > LIMITE_SAQUES:
            print("Operação inválida!! Valor sacado ultrapassa seu limite de saques")
                
        else:
            print(f"Operação aceita!! O valor R${Saque:0.2f} irá ser sacado")
            Extrato += f"\nSaida:   R${Saque:0.2f}"
            return Saque, Extrato ,Numero_saques

def Retirar_Extrato(Extrato):
    print(Extrato)


Menu()