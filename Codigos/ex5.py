
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"


def calculos(a, b):
    print(f"Soma: {soma(a, b)}")
    print(f"Subtração: {subtracao(a, b)}")
    print(f"Multiplicação: {multiplicacao(a, b)}")
    print(f"Divisão: {divisao(a, b)}")


calculos(8,30 )