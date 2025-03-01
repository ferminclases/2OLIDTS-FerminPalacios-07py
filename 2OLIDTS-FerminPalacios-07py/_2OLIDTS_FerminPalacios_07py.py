capacidad = 10
elementos= [0]*capacidad
tope= -1

print("Teclea elemento de la pikla(termina con -1)")
x=0
CLAVE=-1

while x != CLAVE:
    entrada=input()
    if entrada.isdigit():
        x = int(entrada)
        if tope < capacidad -1:
            tope += 1
            elementos[tope] = x
        else:
            print("Exepcion: pila llena")
            break
    elif (int(entrada)==-1):
        print("Finalizado con -1")
        x=int(entrada)
        if tope < capacidad -1:
            tope += 1
            elementos[tope]=x
        else:
            print("Excepcion: pila llena")
            break
        break
    else:
        print("Excepcion: entrada no valida")
if tope >= 0:
    print("Elementos de la pila:", end= " ")
    while tope >= 0:
        x = elementos[tope]
        tope -= 1
        print(x, end= " ")
else:
    print("Pila vacia")



