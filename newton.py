import math

#calcula f(x)
def calcular_funcao(expressao, x):
    expressao = expressao.replace('x', str(x))
    return eval(expressao)

#calcula a derivada
def calcular_derivada(expressao, x):
    h = 10**-5
    derivada =(calcular_funcao(expressao, x+h) - calcular_funcao(expressao, x))/h

    return derivada

def metodo_newton(expressao, chute):
    k=0
    while(calcular_funcao(expressao, chute) > 10**-5):
        chute = chute - (calcular_funcao(expressao, chute)/calcular_derivada(expressao, chute))
        k+=1
    print(f"Numero de interações foi: {k}")
    return chute


def main():
    expressao = input("Digite a expressão da função (por exemplo, x**2):")
    chute = int(input("Digite o seu chute:"))
    resultado = metodo_newton(expressao, chute)

    if(resultado < chute):
        print("Chutou alto...")
    else:
        print("Chutou baixo\n")
    print(">>> O resultado aproximado da raiz é:{:2f}".format(resultado))


   
   
if __name__ == "__main__":
    main()

