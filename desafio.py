menu_logado = """
Escolha uma opção:
1 - Depósito
2 - Saque
3 - Visualizar Extrato
4 - Cadastrar Conta
0 - Sair
"""

menu_inicial="""
1 - Logar
2 - Cadastrar no usuário
0 - Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
is_logged = False
clientes = set()
contas = {}
qtd_conta = 0;


def gerar_extrato(prefixo, valor):
    global extrato
    extrato += f"{prefixo} R${valor:.2f}"

def exibir_extrato():  
    global extrato
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print(f"""
Extrato da conta

{extrato}
              
Saldo disponível: R${saldo:.2f}""")
    
def depositar():
    global saldo
    print(f"Depositar")
    deposito = float(input(f"Informe o valor do depósito: \n"))
    saldo += deposito
    print(f"\nDepósito realizado com sucesso!\nSaldo disponível: R${saldo:.2f}")
    gerar_extrato("\n- Depósito: ", deposito)

def sacar(): 
    if saldo > 0 and numero_saques < LIMITE_SAQUES:
        saque = float(input(f"Informe o valor do saque: \n"))
        efetuar_saque(saque)
    elif numero_saques >= LIMITE_SAQUES:
        print(f"Limite de saque diário atingido.")
    else:
        print(f"\nSaldo insuficidente\nSaldo atual: R${saldo}")

def efetuar_saque(saque):
    global saldo
    global numero_saques
    global limite
    if saque > saldo:
        print(f"Saldo insuficiente\nSaldo disponível: R${saldo:.2f}")
    elif saque > limite:
        print(
            f"""
Saque não permitido.

Seu limite para saque é de R${limite:.2f} 

Saldo disponível: R${saldo:.2f}
"""
        )
    else:
        saldo -= saque
        gerar_extrato("\n- Saque: ", saque)
        numero_saques += 1
        print(f"\nSaque realizado com sucesso!\nSaldo disponível: R${saldo:.2f}")
        return saldo

def cadastrar_cliente(nome, data_nascimento, cpf, endereco):
    global clientes
    cpf = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        # "cpf": cpf,
        "endereco": endereco
    }
    clientes.add(cpf)

def cadastrar_conta(agencia, numero, cliente):
    global contas
    conta = {
            "agencia": agencia,
            "numero": str(numero).zfill(5),
            "cliente": cliente
        }
    contas.add(conta)

def listar_usuários():
    print(clientes)
    
def listar_contas():
    print(contas)


# while True:
#     opcao = input(menu_inicial)
#     if opcao == '1': #Logar
#         if not clientes:
#             print(f"Não há usuários cadastrados.")
#         else:
#             is_logged = True
#             break
#     elif opcao == '2': #Cadastrar Usuário
#         print(f"Cadastro de Usuário\n")
#         cpf = input("CPF: \n")
#         if cpf in clientes:
#             print(f"Usuário já cadastrado.")
#         else:
#             nome = input("Nome completo: \n")
#             data_nascimento = input("Data de nascimento: \n")
#             print(f"Endereço\n")
#             logradouro = input("Logradouro: \n")
#             numero = input("Numero: \n")
#             bairro = input("Bairro: \n")
#             cidade = input("Cidade: \n")
#             estado = input("Estado (sigla)")
#             endereco = {'logradouro': logradouro, 'numero': numero, 'bairro': bairro, 'cidade':cidade, 'estado' : estado }
#             cadastrar_cliente(nome, data_nascimento, cpf, endereco)
#     elif opcao == "0": #Sair
#         print("Obrigado por utilizar o Banco DIO! Volte sempre!")
#         break
#     else:
#         print(
#         f"\nOperação inválida, por favor selecione novamente a operação desejada."
#         )


        
    


while True:
    opcao = input(menu_logado)

    if opcao == "1": #Deposito
        depositar()

    elif opcao == "2": #Saque
        sacar()

    elif opcao == "3": #extrato
        exibir_extrato()

    elif opcao == "4": #Cadastrar conta
        print(f"Cadastro de conta\n")
        cpf = input("CPF: \n")
        if cpf in clientes:
            agencia = input("Agência: \n")
            qtd_conta+=1
            cadastrar_conta(agencia, qtd_conta, cpf)
            
        

    elif opcao == "0": #Sair
            print("Obrigado por utilizar o Banco DIO! Volte sempre!")
            break

    else:
            print(
                f"\nOperação inválida, por favor selecione novamente a operação desejada."
            )
