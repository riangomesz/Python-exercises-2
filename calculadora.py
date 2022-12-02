# Classe criada em Python para realizar calculos utilizando funções
# Função tudo que retorna valor
# Metodo é aquilo que não retorna

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multi(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

    def potencia(self):
        return self.valor_a ** self.valor_b
    
calculadora = Calculadora(20,2)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.multi())
