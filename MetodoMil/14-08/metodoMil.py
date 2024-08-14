import math

def funcao(x):
    return x**3-9*x+3

def fi(x):
    return (x**3)/9+1/3

def mil(x0,delta,n):
    if(math.fabs(funcao(x0)) < delta):
        print("x0: ", x0)
    else:
        k=1
        x1=fi(x0)
        while(math.fabs(funcao(x0)) > delta and math.fabs(x1-x0) > delta and k < n):
            x0=x1
            k+=1
            x1=fi(x0)

        print("Raiz: ", x0)
        print("Iterações: ", k)

if __name__=="__main__":
    x0=float(input("Digite o valor de x0: "))
    delta=float(input("Digite o valor de delta: "))
    n=int(input("Digite o n: "))

    mil(x0,delta,n)