import math

def funcao(x):
    return x**3-9*x+3

def regula(a,b,delta,n):
    if(math.fabs(funcao(a)) < delta or math.fabs(b-a) < delta or math.fabs(funcao(b)) < delta):
        print("a: ", a)
    else:
        k=1
        x= (a*funcao(b)-b*funcao(a)) / (funcao(b)-funcao(a))
        while(math.fabs(funcao(x)) > delta and k < n and math.fabs(b-a) > delta):   
            if(funcao(a)*funcao(x)>0):
                a = x
            else:
                b = x   
            k+=1
            x = (a*funcao(b)-b*funcao(a)) / (funcao(b) - funcao(a))

        print("Raiz: ", x)
        print("Iterações: ", k)

if __name__=="__main__":
    a=float(input("Digite o valor de a: "))
    b=float(input("Digite o valor de b: "))
    delta=float(input("Digite o valor de delta: "))
    n=int(input("Digite o n: "))
    regula(a,b,delta,n)