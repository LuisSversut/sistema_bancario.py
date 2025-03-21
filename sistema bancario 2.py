def menu():
    return '''
--------------MENU--------------
    [D] DEPOSITAR
    [S] SACAR
    [E] EXTRATO
    [NU] NOVO USUARIO
    [NC] NOVA CONTA
    [F] FINALIZAR
    
'''

def deposito(saldo, extrato, /):
    valor = int(input("Deposito R$"))

    if valor > 0:
        saldo += valor
        extrato += f"Deposito R${valor:.2f}\n"
        print("\nDeposito realizado com sucesso!")

    else:
        print("VALOR INVALIDO")

    return saldo, extrato

def saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("SAQUE R$"))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente!")

    elif excedeu_limite:
        print("Valor acima do limite permitido para saque!")

    elif excedeu_saques:
        print("Numero maximo de saques atingido!")

    elif valor >0:
        saldo -= valor
        extrato += f"Saque R${valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Valor invalido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo R${saldo:.2f}")

def novo_usuario(usuarios):
    cpf = int(input("CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Usuario ja existe!")
        return
    
    nome = str(input("Nome: "))
    data_nascimento = str(input("Data de nasacimento: "))
    endereco = str(input("Endereço (rua, nro - bairro - cidade/estado): "))

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = int(input("CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario não encontrado, criação de conta encerrada!")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = "" 
    numero_saques = 0
    limite = 500
    usuarios = []
    contas = []
    while True:
        opcao = str(input(menu()))
        if opcao == "d":
            saldo, extrato = deposito(saldo, extrato)
        
        elif opcao == "s":
            saldo,extrato = saque(
                saldo=saldo, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES,)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            novo_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "f":
            break

        else:
            print("Opção invalida!")



main()