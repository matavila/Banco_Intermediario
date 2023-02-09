Texto_Entrada = """
        <-----------------MENU DE ENTRADA--------------------->

        [0] = Criar Conta
        [1] = Entrar
        [2] = Lista de Contas
        [3] = Sair

        <------------------------------------------------------>

    """  
Texto_Entrada_Conta = """
        <-----------------MENU DAS CONTAS--------------------->

        [1] = Lista dos Usuários (adm)
        [2] = Lista de Logins

        <------------------------------------------------------>

    """ 
menu = """
    <-----------------MENU--------------------->

    [0] = Depositar
    [1] = Sacar
    [2] = Extrato
    [3] = Sair
    [4] = Conta

    <------------------------------------------>
"""
def Sala_Login():
    Clientes = {}
    Logins = []
    Saldo = 0

    while True:
        Digito = Menu_Entrada()
        if Digito == 0:
            print("<---------CRIANDO CONTA--------->")
            Conta, Usuario = Criar_Conta(Clientes, Saldo)
            Clientes.update(Conta)
            Logins.append(Usuario)
            print("<---CONTA CRIADA COM SUCESSO---->")

        elif Digito == 1:
            print("<------------LOGIN-------------->")
            Situacao,Usuario_Banco = Verificar_Conta(Logins)
            if Situacao == True:
                Sistema_Banco(Usuario_Banco,Saldo,Clientes)
                break

            else:
                break

        elif Digito == 2:
            Lista_Contas(Clientes, Logins)

        elif Digito == 3:
            break

        else:
            print("--------------------------")
            print("Selecione uma opçao valida")
            print("--------------------------")

            Sala_Login()


def Menu_Entrada():
    print(Texto_Entrada)
    opcao = int(input("DIGITE SUA OPÇÃO:  "))
    return opcao

def Criar_Conta(Clientes, Saldo):
    Login = input("Digite o seu Login: ")

    if Login in Clientes:
        print("<------------CONTA JA EXISTENTE------------->")
        return

    Nome =input("Digite o seu nome: ")
    Data = input("Digite sua data de nascimento: ")
    Saldo = 0

    Novo = {f"{Login}": {"Nome":f"{Nome}", "Nascimento":f"{Data}","Saldo":Saldo}}
    return Novo, Login

def Lista_Contas(Clientes, Logins):
    print(Texto_Entrada_Conta)
    opcao = int(input("DIGITE SUA OPÇÃO:  "))

    if opcao == 1:
        for chaves in Clientes.items():
            print(chaves)
    elif opcao == 2:
        for i in Logins:
            print(i)
    else:
        print("--------ERROR: Digite um número valido----------")
        Lista_Contas()

def Verificar_Conta(Logins):
    Login = input("Digite o seu Login: ") 
    if Login in Logins:
        return True,Login

    else:
        print("-----------------")
        print("Conta Inexistente")
        print("-----------------")
        return False

#<---------------------------------------------------BANCO------------------------------------------------------------------>
def Sistema_Banco(Usuario,Saldo,Clientes):
    Saldo = Saldo
    LIMITE = 800
    Extrato =""
    Nome = Usuario
    Saque = 0
    Numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        Digito = Menu_Banco()

        if Digito == 0:
            """
            Erro que acontece é que quando pego para ver a conta, o saldo sai com o resultado
            de todas as movimentações + meu primeiro depósito
            """
            print("<------------Depositar------------->")
            Entrada = int(input("Digite o valor a ser depositado:  "))
            Saldo, Extrato = Depositar(Saldo, Entrada, Extrato)
            Clientes[f"{Nome}"]["Saldo"] += Saldo
            print()
            Sistema_Banco(Usuario,Saldo,Clientes)


        elif Digito == 1:
            """
            Aqui devido ao saldo do cliente ser igualado ao saldo após a movimentação de saque, o resultado final
            do saldo do cliente permance certo, porêm se eu não passar por essa etapa dar o erro citado acima
            """
            print("<------------Sacar------------->")
            Saque, Extrato, Numero_saques = Sacar(Saldo,Saque, Extrato, LIMITE, Numero_saques, LIMITE_SAQUES)
            Saldo-= Saque
            Clientes[f"{Nome}"]["Saldo"] = Saldo
            print()
            print(f"O seu saldo é de {Saldo}")
            print("<------------Saque com Sucesso------------->")
            print()
            Sistema_Banco(Usuario,Saldo,Clientes)

        elif Digito == 2:
            """
            O extrato mostra o valor certo do Saldo, fazendo ou não qualquer uma das operações, porêm eu não 
            consigo mas ver no extrato essas movimentações
            """
            print("=====================Extrato====================")
            Extrato = Retirar_Extrato(Extrato)
            print(f'\n Saldo: R${Saldo:0.2f}')
            print("================================================")
            Sistema_Banco(Usuario,Saldo,Clientes)

        elif Digito == 3:
            print("Sair")
            break

        elif Digito == 4:
            BancoDados(Clientes)

        else:
            print("<------------ERRO------------->")
            Menu_Banco()

        return Saldo
    
    

def Menu_Banco():
    print(menu)
    opcao = int(input("DIGITE SUA OPÇÃO:  "))
    return opcao

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

Sala_Login()

