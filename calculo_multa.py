
# Programa que recebe a velocidade média de um carro, e diz se o mesmo irá angariar uma punição 
# se o mesmo tiver ultrapassado a velocidade média imposta naquela região

velocidade = float(input("Informe a velocidade média de seu carro:"))
kmAcima = velocidade - 80


if velocidade > 80:
    multa = kmAcima * 5
    print ("Sua multa foi de "+str(multa)+" reais")
else:
    print("Você não recebeu nenhuma multa")
