"""palabra=input("Ingresar una palabra ")
lista=[]
for numero in range(len(palabra)):
    lista.append(palabra[numero])
print(lista)"""

"""dieznumeros=input("Ingresar 10 numeros ")
lista=[]
for numero in range(len(dieznumeros)):
    lista.append(dieznumeros[numero])
print(lista)"""

lista=[]
for numero in range(10):
    numeros=int(input("ingresar un numero:"))
    lista.append(numeros)

menor=lista[0]
for numero in range (len(lista)):
    if lista[numero]<menor:
       menor=lista[numero]
print(f"el numero menor es {menor}")





tupla=(1,2,3,4,5,6,7)
Numero=input("ingresar un numero")
for numero in range(len(tupla)):
    if tupla[numero]==Numero:
print(numero)