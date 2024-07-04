from exercício import Conta

conta = Conta("001", 1000)

nome = input("Olá. Digite o seu nome: ")

menu = f"""
Olá {nome}. Bem vindo á sua conta.

O que deseja fazer:

[1] - Visualizar conta;
[2] - Sacar;
[3] - Depositar;
[4] - Sair;

Digite a opção: """

while True:
    opcao = int(input(menu ))

    if opcao == 1:
        print(f'Valor atual da conta: {conta.mostrar_saldo()}')
        input("Tecle mais uma vez para voltar ao menu")

    elif opcao == 2:
        valor = float(input('Digite o valor a sacar: '))
        conta.sacar(valor)
        input("Tecle mais uma vez para voltar ao menu")

    elif opcao == 3:
        valor = float(input('Digite o valor a depositar: '))
        conta.depositar(valor)
        input("Tecle mais uma vez para voltar ao menu")

    else:
        print(f'Obrigado por usar o nosso banco, {nome}')
        break