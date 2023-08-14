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
        extrato += f"\n Depósito: R${deposito:.2f}"
        print(f"Saldo disponível: R${saldo:.2f}")

    if opcao == "2":
        if saldo != 0 :
            saque = float(input(f"Informe o valor do saque: \n"))
            if saque>saldo:
                print(f"Saldo insuficiente \n Saldo disponível: R${saldo:.2f}")
            elif numero_saques >= LIMITE_SAQUES:
                print(f"Limite de saques diários atingido.")
            elif saque>limite:
                print(f"""Operação não realizada...
Seu limite para saque é de R${limite:.2f} 
Saldo disponível: R${saldo:.2f}""")                
            else: 
                saldo -= saque
                extrato += f"\n Saque: R${saque:.2f}"
                numero_saques+=1            
                print(f"Saldo disponível: R${saldo:.2f}")
        else: 
            print(f"""Saldo insuficiente
Saldo disponível: R${saldo:.2f}""") 

    if opcao == "3":
        if extrato == '' :
            print("Não foram realizadas movimentações.")
        else:
            print(f"Saldo disponível: R${saldo:.2f} \n {extrato}")        

    if opcao == "0":
        print("Obrigado por utilizar o Banco DIO! Volte sempre!")
        break

    if opcao != '0' and opcao != '1' and opcao != '2' and opcao != '3' :
        print(f"Operação inválida, por favor selecione novamente a operação desejada.")
