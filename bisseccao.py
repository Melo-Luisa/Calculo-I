import math

def calcular_funcao(expressao, x):
    # irá susbstituir o x pelo intervalo
    expressao = expressao.replace('x', str(x))
    # Eval tem como objetivo calcular a função
    return eval(expressao)

def metodo_da_bisseccao(expressao, a, b):
    if calcular_funcao(expressao, a) * calcular_funcao(expressao, b) > 0:
        print("Não tem numeros para onde essa função seja 0")
        return None
    else:
        ponto_medio = (a + b) / 2
        while calcular_funcao(expressao, ponto_medio) > 10**-5:
            ponto_medio = (a + b) / 2
            if calcular_funcao(expressao, ponto_medio) * calcular_funcao(expressao, a) < 0:
                b = ponto_medio
            else:
                a = ponto_medio
    return ponto_medio
def main():
    expressao = input("Digite a expressao da funcao (por exemplo, x**3+x**2-x+2): ")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    
    resultado = metodo_da_bisseccao(expressao, a, b)

    if resultado is not None:
        print("O resultado aproximado da raiz é:", resultado)
    else:
        print("Não foi possível encontrar a raiz dentro da precisão desejada.")

if __name__ == "__main__":
    main()

