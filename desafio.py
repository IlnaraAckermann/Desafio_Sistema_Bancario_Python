menu = """
Escolha uma opção:
1 - Depósito
2 - Saque
3 - Visualizar Extrato
0 - Sair
"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def gerar_extrato(prefixo, valor):
    global extrato
    extrato += f"{prefixo} R${valor:2f}"
    return extrato

def depositar(deposito):
    global saldo
    saldo += deposito
    print("\nDepósito realizado com sucesso!\n")
    print(f"Saldo disponível: R${saldo:.2f}")
    gerar_extrato("\n- Depósito: ", deposito)
    return saldo

def sacar(saque):
    global saldo
    global numero_saques
    global limite
    if saque > saldo:
        print(f"Saldo insuficiente\nSaldo disponível: R${saldo:.2f}")
    elif saque > limite:
        print(f"""
Saque não permitido.

Seu limite para saque é de R${limite:.2f} 

Saldo disponível: R${saldo:.2f}
""")
    else:
        saldo -= saque
        gerar_extrato("\n- Saque: ", saque)
        numero_saques += 1
        print(f"\nSaque realizado com sucesso!\nSaldo disponível: R${saldo:.2f}")
        return saldo



while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        deposito = float(input(f"Informe o valor do depósito: \n"))
        depositar(deposito)

    elif opcao == "2":
        if saldo > 0 and numero_saques < LIMITE_SAQUES:
            saque = float(input(f"Informe o valor do saque: \n"))
            sacar(saque)
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saque diário atingido.")
        else:
            print(f"\nSaldo insuficidente\nSaldo atual: R${saldo}")
           
    elif opcao == "3":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(
                f"""{extrato}
                  
Saldo disponível: R${saldo:.2f}"""
            )

    elif opcao == "0":
        print("Obrigado por utilizar o Banco DIO! Volte sempre!")
        break

    else:
        print(
            f"\nOperação inválida, por favor selecione novamente a operação desejada."
        )
