velocidade = float(input("Informe a velocidade média de seu carro:"))
kmAcima = velocidade - 80


if velocidade > 80:
    multa = kmAcima * 5
    print ("Sua multa foi de "+str(multa)+" reais")
else:
    print("Você não recebeu nenhuma multa")