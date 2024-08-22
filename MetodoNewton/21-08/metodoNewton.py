import math

def funcao(x):
    return x+math.log(x)

def derivada(x):
    return 1+1/x

def newton(x0,delta,n):
    if(math.fabs(funcao(x0)) > delta):
        k=1
        fxlinha= derivada(x0)
        x1=x0-funcao(x0)/fxlinha
        fx = funcao(x1)
        while(math.fabs(fx) > delta and math.fabs(x1-x0) > delta and k < n):
            k+=1
            x0=x1
            fxlinha = derivada(x0)
            x1=x0-fx/fxlinha
            fx=funcao(x1)
        print("Raiz: ", x1)
    else:
        print("Raiz: ", x0)
        print("Iterações: ", k)

if __name__=="__main__":
    x0=float(input("Digite o valor de x0: "))
    delta=float(input("Digite o valor de delta: "))
    n=int(input("Digite o n: "))
    newton(x0,delta,n)