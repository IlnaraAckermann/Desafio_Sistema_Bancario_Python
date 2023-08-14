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
        print("saque")
   

    if opcao == "3":
        print("extrato")         

    if opcao == "0":
        print("Obrigado por utilizar o Banco DIO! Volte sempre!")
        break

else:
    print(f"Operação inválida, por favor selecione novamente a operação desejada.")
