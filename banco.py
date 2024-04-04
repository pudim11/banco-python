Menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    op= input(Menu)
    
    if op == "d":
        
            valor = float(input("digite um valor:"))
            if(valor >= 1):
                saldo += valor
                extrato += f"Depósito de {valor:.2f} reais\n"
                print(f"seu saldo é: {saldo:.2f}")
            else:
                print("Valor incorreto")

    
    elif op == "s":
        valor = float(input("digite um valor:"))
        if saldo >= valor and numero_saques != LIMITE_SAQUES and valor < 500:
            saldo -= valor
            extrato += f"Saque de {valor:.2f} reais\n"
            numero_saques += 1
            print(f"seu saldo é: {saldo:.2f}")
        elif saldo < valor:
            print("Saldo insuficiente")
        else:
            print("Limite de saques excedido")
    
    elif op == "e":
        print(extrato)
    elif op == "q":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a seleão desejada")