# Desafio Python DIO - Sistema Bancário 💰

Bem-vindo ao Desafio Python da Digital Innovation One! Neste desafio, você vou criar um modelo de sistema bancário simples com as operações de saque, depósito e visualização de extrato. Vamos começar!

## Versão 1.0 - Sistema Bancário

### Descrição

Nesta primeira versão do sistema bancário, estamos criando um modelo simplificado para um único usuário, sem a necessidade de identificação de agência ou conta. O sistema permitirá que o usuário realize operações de saque, depósito e visualize o extrato das transações.

### Funcionalidades

1. **Depósito**: O usuário poderá fazer depósitos em sua conta. O valor do depósito será armazenado e somado ao saldo disponível.

2. **Saque**: O usuário poderá fazer saques de sua conta, com algumas restrições. O valor máximo de saque por vez será de R$500,00, e o usuário só poderá fazer até 3 saques por dia. O valor do saque será deduzido do saldo disponível.

3. **Visualização de Extrato**: O usuário poderá visualizar seu extrato, que mostrará o valor total, bem como os depósitos e saques feitos. Se não houver movimentações, a mensagem "Não foram realizadas movimentações" será exibida.

### Requisitos

- Verificar o valor do saque e se ele respeita o limite diário e o valor máximo por saque.
- Verificar se o valor do saque é menor ou igual ao saldo disponível.
- Verificar a quantidade de saques feitos no dia.

### Exemplo de Saída

```plaintext
Bem-vindo(a) ao Banco DIO!

Escolha uma opção:
1 - Depósito
2 - Saque
3 - Visualizar Extrato
0 - Sair

Opção: 2

Informe o valor do saque: 300.00

Saque realizado com sucesso!

Saldo disponível: R$ 700.00

Escolha uma opção:
1 - Depósito
2 - Saque
3 - Visualizar Extrato
0 - Sair

Opção: 3

Extrato:

- Depósito: R$ 1000.00
- Saque: R$ 300.00

Saldo Total: R$ 700.00

Escolha uma opção:
1 - Depósito
2 - Saque
3 - Visualizar Extrato
0 - Sair

Opção: 0

Obrigado por utilizar o Banco DIO! Volte sempre!
```

Se você achou este repositório útil e interessante, por favor, considere deixar uma estrela ⭐🤩
Estou aberta a perguntas e sugestões para melhorias. Sinta-se à vontade para compartilhar seus comentários e ideias. Sua opinião é muito importante para mim!

Vamos continuar aprendendo e crescendo na jornada de programação. Até a próxima e bons estudos! 🌟🚀🐍
