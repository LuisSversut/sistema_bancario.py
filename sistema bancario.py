menu = """
Selecione uma opção

[1] Saque
[2] Deposito
[3] Extrato
[0] Encerrar
"""

saldo = 0
deposito = 0
quantidade_saque = 3
extrato = ""

while True:
    print(menu)
    opcao = int(input("Opção: "))

    #Defindo opçoes de saque

    if opcao == 1:
        if quantidade_saque <= 0:
            print("Limite de saques diario atingido")
            continue
        saque = int(input("Valor: R$ "))
        if saque > 0 and saque <= saldo and quantidade_saque > 0:
            if saque <= 500:
                extrato += f"Saque: R$ {saque:.2f}\n"
                saldo -= saque
                quantidade_saque -= 1
            else:
                print("Valor do saque acima do permitido")
        elif saque <= 0:
            print("Valor para saque deve ser maior que R$ 0")
        elif saque > saldo:
            print("Saldo insuficiente")

    #Definindo opçoes de deposito

    elif opcao == 2:
        deposito = int(input("Valor do deposito: R$ "))
        if deposito > 0:
            print("Deposito realizado")
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor de deposito invalido")

    #Definindo opçoes de extrato

    elif opcao == 3:
        print("\n--------------------EXTRATO---------------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo R$ {saldo:.2f}")
        print("------------------------------------------------")

    #Finalizando operação

    elif opcao == 4:
        print("Volte sempre")
        break

    #Se usuario escolher uma opçao invalida

    else:
        print("Opção invalida")
