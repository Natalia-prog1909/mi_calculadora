def sumar(a: float,b: float) -> float:
    #Suma dos numeros.
    return a + b

def restar(a: float,b: float) -> float:
    #Restar el segundo número al primero.
    return a - b

def multiplicar(a: float,b: float) -> float:
    #Multiplica dos numeros.
    return a * b

def dividir(a: float, b: float) -> float:
    #Divide el primer número por el segundo.
    if b ==0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__=="__main__":
    print(sumar(2,3)) #5
    print(restar(5,1)) #4
    print(multiplicar(4,2)) #8
    print(dividir(10,2)) #5.0


def potencia(a: float, b: float)-> float:
    # calcula a elevado a la b.
    return a**b
if __name__=="__main__":
    print(potencia(4,2))#16

def elevar_al_cubo (a: float, b: float)-> float:
    # calcula a elevado al cubo b.
    return a**3
if __name__=="__main__":
    print(elevar_al_cubo(8,3))#512
