maior = 0
menor = 0
vendas = []

for i in range(0,3):
    vendas.append(int(input("Informe o valores das vendas: ")))
    
    if i == 0:
        maior = menor = vendas[i]
    
    elif vendas[i] > maior:
        maior = vendas[i]
    
    elif vendas[i] < menor:
        menor = vendas[i]

print(menor,maior)

print(vendas)
