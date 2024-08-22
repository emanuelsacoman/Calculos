import math

def funcao(x):
    return x**3-0.5

def secante(x0,x1,delta,n):
    if(math.fabs(funcao(x0)) < delta):
        print("x0: ", x0)
    else:
        k=1
        x2=1
        while(math.fabs(funcao(x2)) > delta and k < n):
            x2= x1-funcao(x1)*(x1-x0)/(funcao(x1)-funcao(x0))
            x0=x1
            x1=x2            
            k+=1

        print("Raiz: ", x2)
        print("Iterações: ", k)

if __name__=="__main__":
    x0=float(input("Digite o valor de x0: "))
    x1=float(input("Digite o valor de x1: "))
    delta=float(input("Digite o valor de delta: "))
    n=int(input("Digite o n: "))
    secante(x0,x1,delta,n)