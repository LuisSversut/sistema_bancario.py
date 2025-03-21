from datetime import datetime, date

#Definindo data

data_completa = datetime.now()
data_atual = data_completa.date()
data = 0

#Definindo variaveis

trasacoes = 0
saques = 0
saldo = 0
extrato = ""

menu = """
Selecione uma opção

[1] Saque
[2] Deposito
[3] Extrato
[0] Encerrar
"""
#Estrutra

while True:
    #Verificando transaçoes diarias
    if data_atual != data:
        data = data_atual
        transacoes = 10
        saques = 3
    if transacoes == 0:
        print("Limite de transações diarias atingido!")
        break
    else:
        print(menu)
        opcao = int(input("Opção: "))

    #Defindo opçoes de saque

        if opcao == 1:
            if saques <= 0:
                print("Limite de saques diario atingido")
                continue
            saque = int(input("Valor: R$ "))
            if saque > 0 and saque <= saldo and saques > 0:
                if saque <= 500:
                    nova_data = datetime.now()
                    data_hora = nova_data.strftime("%d/%m/%Y %H:%M")
                    extrato += f"Saque: R$ {saque:.2f} " + data_hora + "\n"
                    saldo -= saque
                    transacoes -= 1
                    saques -= 1
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
                transacoes -= 1
                nova_data = datetime.now()
                data_hora = nova_data.strftime("%d/%m/%Y %H:%M")
                extrato += f"Depósito: R$ {deposito:.2f} " + data_hora + "\n"
            else:
                print("Valor de deposito invalido")

    #Definindo opçoes de extrato

        elif opcao == 3:
            print("\n--------------------EXTRATO---------------------")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo R$ {saldo:.2f}")
            print("------------------------------------------------")
            transacoes -= 1

    #Finalizando operação

        elif opcao == 4:
            print("Volte sempre")
            break

    #Se usuario escolher uma opçao invalida

        else:
            print("Opção invalida")
