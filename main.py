def ultima_parada(combustivel,consumo,postos_de_gasolina):
    pass
    
    postos_de_gasolina = [2,10.2,15,22]
    alcance = (combustivel * consumo) - 1
    
    if alcance >= 0 and alcance <= 2 :
      return 2
    elif alcance > 2 and alcance <= 10.2:
      return 10.2
    elif alcance > 10.2 and alcance <= 15:
      return 15
    elif alcance > 15 and alcance <= 22:
      return 22
    else:
      return -1

print(ultima_parada(2,8,[2,10.2,15,22]))

