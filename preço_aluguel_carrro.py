# Programa que recebe os km percorridos e dias que o carro ficou alugado pelo cliente
# E depois retorna o valor em reais do aluguel do carro
$$$$$$$$$$$$$$$$



km_pecorrido = float(input("Informe os km percorridos: "))
dias_alugados = int(input("Informe quantos dias ele foi alugado: "))
preco = (60*dias_alugados) + (0.15 * km_pecorrido)
print("O valor a pagar foi de: R$",preco)

