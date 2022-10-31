km_pecorrido = float(input("Informe os km percorridos: "))
dias_alugados = int(input("Informe quantos dias ele foi alugado: "))
preco = (60*dias_alugados) + (0.15 * km_pecorrido)
print("O valor a pagar foi de: R$",preco)