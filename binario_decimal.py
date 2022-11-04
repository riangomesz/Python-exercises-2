# Código que recebe um valor binário, depois transforma-o em uma valor decimal

def calcula_numero_da_senha(senha):
    pass

    senha = 1011010100 

    n = len(str(senha))
    valor_digitado = senha
    decimal = 0
    i = 0

    while n >= 0:
  
        resto = senha % 10
        decimal = decimal + (resto * (2**i))
        n = n - 1
        i = i + 1
        senha = senha // 10
    
    return decimal 
    
print(calcula_numero_da_senha(1011010100))




