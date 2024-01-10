sinal = int(input("Digite o valor do sinal: "))
aposta = int(input("Digite o valor da aposta: "))
invest_total = sinal + aposta
print(f"O seu investimento total será de: {invest_total}")
lucro = aposta * 2
print(f"O retorno do investimento será de: {lucro}")
salvo = lucro - invest_total
print(f"O valor salvo após a retirada do seu investimento inicial será: {salvo}")
salvo_apos_deducao = salvo - sinal
print(f"O seu lucro após o pagamento do sinal na 1 vez será de: {salvo_apos_deducao}")
i = 2
vezes = int(input("Quantas vezes você vai entrar nessas operações: "))
while i <= vezes:
    lucro = salvo_apos_deducao * 2
    salvo_apos_deducao = lucro - sinal
    print(f"O seu lucro após o pagamento do sinal na {i} vez será de: {salvo_apos_deducao}")
    i += 1
else:
    print("O programa acabou")