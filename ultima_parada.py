

def ultima_parada(combustivel,consumo,postos_de_gasolina):
    pass
    
    alcance = combustivel * consumo
    postos_de_gasolina.sort()
    postos_de_gasolina.reverse()
    i=0

    if postos_de_gasolina:
      for posto in postos_de_gasolina:
        if alcance >= posto:
            return posto
      return -1 

print(ultima_parada(2,8,[9,11,15,22]))
