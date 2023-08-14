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

while True:
    opcao = input(menu)
    if opcao == "1":
        deposito = float(input(f"Informe o valor do depósito: \n"))
        saldo += deposito
        extrato += f"\n- Depósito: R${deposito:.2f}"
        print("\nDepósito realizado com sucesso!\n")
        print(f"Saldo disponível: R${saldo:.2f}")

    elif opcao == "2":
        if saldo != 0:
            saque = float(input(f"Informe o valor do saque: \n"))
            if saque > saldo:
                print(f"Saldo insuficiente \nSaldo disponível: R${saldo:.2f}")
            elif numero_saques >= LIMITE_SAQUES:
                print(f"Limite de saques diários atingido.")
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
                extrato += f"\n- Saque: R${saque:.2f}"
                numero_saques += 1
                print("\nSaque realizado com sucesso!\n")
                print(f"Saldo disponível: R${saldo:.2f}")
        else:
            print(
                f"""
Saldo insuficiente

Saldo disponível: R${saldo:.2f}
"""
            )

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
