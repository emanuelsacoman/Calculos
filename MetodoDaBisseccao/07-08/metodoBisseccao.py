import math

def funcao(x):
    #return x**3-3*x**2-6*x+8
    #return x**3-10
    #return math.e**(-x**2)-math.cos(x)
    #return x**2-5
    return x**2+0.96*x-2.08

def bisseccao(a,b,delta,n):
    k=0
    if (math.fabs(b-a)<delta):
        print("Raiz:" ,b)
    else:
        while(math.fabs(b-a) > delta and k<n):
            k+=1
            finicio=funcao(a)
            meio=(a+b)/2.0
            fmeio=funcao(meio)
            if(finicio*fmeio<0):
                b=meio
            else:
                a=meio
    print("Raiz: ", meio)
    print("Número iteracoes: ", k)

if __name__=="__main__":
    a=float(input("Digite o valor de a: "))
    b=float(input("Digite o valor de b: "))
    delta=float(input("Digite o valor de delta: "))
    n=int(input("Digite o n: "))

    bisseccao(a,b,delta,n)
