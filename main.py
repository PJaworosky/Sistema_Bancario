
# Definindo as variáveis iniciais do sistema
saldo = 0
LIMITE_SAQUE_VALOR = 500
LIMITE_SAQUES_DIARIOS = 3
numero_saques_hoje = 0
extrato = ""

# Loop principal para manter o sistema rodando
while True:
    menu = """
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

=> """
    
    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado deve ser positivo.")
        except ValueError:
            print("Operação falhou! Valor inválido. Por favor, insira um número.")
    
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            
            excedeu_saldo = valor > saldo
            excedeu_limite_valor = valor > LIMITE_SAQUE_VALOR
            excedeu_limite_saques = numero_saques_hoje >= LIMITE_SAQUES_DIARIOS
            
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            
            elif excedeu_limite_valor:
                print("Operação falhou! O valor do saque excede o limite de R$500.00.")
            
            elif excedeu_limite_saques:
                print("Operação falhou! Você já atingiu o limite de 3 saques diários.")
            
            elif valor > 0:
                saldo -= valor
                numero_saques_hoje += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print("Saque realizado com sucesso!")
            
            else:
                print("Operação falhou! O valor informado deve ser positivo.")
        except ValueError:
            print("Operação falhou! Valor inválido. Por favor, insira um número.")
            
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato, end="")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        print("Obrigado por usar nosso sistema bancário. Até mais!")
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")