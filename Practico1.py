"""Mensaje simple: Almacene un mensaje en una variable e imprímalo en pantalla. Después cambie el valor del
mensaje e imprímalo nuevamente."""
Mensaje="Guardar Mensaje"
print(Mensaje)

"""Almacene el nombre de una persona en una variable, imprima un mensaje para esa persona. Por ejemplo “Hola
Fede, ¿e gustaría aprender a programar?”"""
Nombre="Gustavo"
print(f"Hola {Nombre},¿Te gustaria aprender a programar?")

"""3. El número ocho: Escriba una suma, resta, multiplicación y división que resulten cada una en el número ocho.
Asegúrese de utilizar la función print() para ver los resultados en pantalla. Un ejemplo de línea es el siguiente:"""
"""EN ESTE EJERCICIO ME FALTO COMO HACER EL SALTO DE LINEA"""
suma=int(5+3)
resta=int(9-1)
multiplicacion=int(2*4)
division=int(64/8)
print(suma)
print(resta)
print(multiplicacion)
print(division)

"""4. Cree cuatro variables llamadas mi_entero, mi_decimal, mi_string y mi_booleano. Asigne a cada variable un valor del
tipo que le corresponda. Luego muestre en pantalla el tipo de cada variable usando la función type() combinando
todo con la función print():"""

"""mi_entero=int(input("Por favor ingresar un numero entero "))
mi_decimal=float(input("ahora ingresa un numero con decimal "))
mi_string=str(input("aca una palabra o cualquier caracter "))
mi_booleano=bool(input("1<1"))
print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))"""

"""mi_entero=int(input("Por favor ingresar un numero entero "))
entero=mi_entero
mi_decimal=float(input("Ahora ingresa un numero con decimal "))
decimal=mi_decimal
mi_string=str(input("Aca una palabra o cualquier caracter "))
string=mi_string
mi_booleano=bool(input("1==1.0 ?"))
booleano=mi_booleano
print(type(entero))
print(type(decimal))
print(type(string))
print(type(booleano))"""

mi_entero=30
mi_decimal=52.3
mi_string=str("tres")
mi_booleano=1<6
print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))

"""5. Escriba un programa que acepte un numero decimal como entrada y lo imprima sin lugares decimales."""
Numero=float(input("Por favor ingresa un numero decimal"))
NUMERO=int(Numero)
print(NUMERO)

"""¿Cuál es la salida de las siguientes expresiones? A ESTE NO LO ENTENDI
1 != 2
Salida: true
True == 1
Salida:error
False != False
Salida: false
False > 0
Salida:error
1.0 < 1
Salida: falso
“test” == “test”
Salida:true
1.0 >= 1
Salida:true"""

"""7. (Opcional) Escriba un programa que le pida al usuario que ingrese nombre y edad. Luego muestre un mensaje
donde le informe el año en que va a cumplir 100."""

Nombre=str(input("Ingresa tu nombre por favor "))
Edad=int(input("Ahora tu edad "))
año=100-Edad
prediccion=año+2023
print(f"Hola {Nombre} en el {prediccion} vas a estar cumpliendo 100 años!!!")

"""8. (Opcional) Escriba un programa que permita convertir una temperatura en Celsius a la escala Farenheit. La
fórmula es:
Fahrenheit = (9.0/5.0) x Celsius + 32"""

temperaturacelsius=int(input("Ingresa la temperatura a convertir "))
Fahrenheit=(9.0/5.0)*(temperaturacelsius+32)
print(f"La temperatura {temperaturacelsius}° celsius, en fahrenheit es {Fahrenheit}")

"""9. (Opcional) Calculadora simple: Cree un programa capaz de pedir dos números al usuario y devolver el resultado
de la suma, resta, multiplicación y división entre los mismos. Por ejemplo, si los números son 3 y 5, la calculadora
nos devolvería: 3+5; 3-5; 3*5 y 3/5. Pruebe también expandir su calculadora y agregar nuevas operaciones, tales
como la potenciación o la división entera"""

Numero1=int(input("Por Favor ingresa el primer numero "))
Numero2=int(input("Ahora ingresar el segundo numero, y a continuacion veras las operaciones que realiza esta calculadora "))
suma=Numero1+Numero2
Resta=Numero1-Numero2
multiplicacion=Numero1*Numero2
dividir=Numero1/Numero2
print(f"{Numero1}+{Numero2} es = {suma}")
print(f"{Numero1}-{Numero2} es = {Resta}")
print(f"{Numero1}x{Numero2} es = {multiplicacion}")
print(f"{Numero1}/{Numero2} es = {division}")