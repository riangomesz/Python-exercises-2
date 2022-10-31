# Programa que calcula o valor a ser pago pelo cliente
# Baseando-se nos km pecorridos e no número de dias que ele foi utilizado




km_pecorrido = float(input("Informe os km percorridos: "))
dias_alugados = int(input("Informe quantos dias ele foi alugado: "))
preco = (60*dias_alugados) + (0.15 * km_pecorrido)
print("O valor a pagar foi de: R$",preco)
