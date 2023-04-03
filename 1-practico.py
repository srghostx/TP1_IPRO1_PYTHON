#by:

#████████████████████████████████████████████
#██▀▄─██▄─▄███▄─▄▄─█▄─▀─▄█▄─▀─▄█▄─▄▄─███▄▄▄░█
#██─▀─███─██▀██─▄█▀██▀─▀███▀─▀███─▄█▀████▄▄░█
#▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄█▄▄▀▄▄█▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▀


#----------------------------------------------------------------
PI = 3.14
radioEsfera = float(input("ingrese el valor del radio:"))
volumenEsfera = 4/3*PI*radioEsfera**3

print("El volumen de la esfera es", volumenEsfera) 

# -------------------------------------------------------------
precio = float(input("Ingrese el precio del producto: "))
unidades = int(input("Ingrese el número de unidades a comprar: "))

importe = precio * unidades

# Imprimir el resultado
print("El importe de dinero a pagar es:", importe)

#-------------------------------------------------------------

# Dado el siguiente código en Python:
# Muestre el resultado con n = 2 y m = 5
#● ¿Puede obtener un resultado para cualquier valor de m?
#● ¿Qué operador utiliza para calcular el resto?
#● Modifique el código quitando str() en la 3er línea, ¿qué sucede?

n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n+" entre "+m+" da un cociente "+str(int(n)//int(m)) + " y un resto " + str(int(n) % int(m)))

#__________________________________________________________________

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
z = int(input("Ingrese el valor de z: "))
raiz_cubica = (x/(y-z))**(1/3)

# Calcular el valor de la e1
e1 = 3*x/y + -y/z*5
print("Valor de e1:", e1)
print("Tipo de e1:", type(e1))

# Calcular el valor de la e2
e2 = 3.14 * x**2 - 1/2 * raiz_cubica
print("Valor de e2:", e2)
print("Tipo de e2:", type(e2))

#___________________________________________________________________

deposito = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))

interes_anual = 0.04
ahorro_anual = deposito * interes_anual
#primer año
total_ahorro = deposito + ahorro_anual
print(f"El ahorro después del primer año es de: 1{round(total_ahorro, 2)}")

#segundo año
total_ahorro += ahorro_anual
print(f"El ahorro después del segundo año es de: {round(total_ahorro, 2)}")

#tercer año
total_ahorro += ahorro_anual
print(f"El ahorro después del tercer año es de: {round(total_ahorro, 2)}")

#------------------------------------------------------------------------

ladoA = float(input("Ingrese la longitud del lado A del rectángulo: "))
ladoB = float(input("Ingrese la longitud del lado B del rectángulo: "))

perimetro = 2 * (ladoA + ladoB)
superficie = ladoA * ladoB

print(f"El perímetro del rectángulo es: {perimetro}")
print(f"La superficie del rectángulo es: {superficie}")

#_______________________________________________________________________

cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
print(f"La hipotenusa es: {hipotenusa:.2f}")

#-----------------------------------------------------------------------

pesos = float(input("Ingrese una cantidad de pesos Argentinos: "))

dolares = pesos / 202.30
euros = pesos / 214.30

print(f"{pesos} pesos Argentinos son equivalentes a {dolares:.3f} dólares y a {euros:.3f} euros.")

#---------------------------------------------------------------------------

anguloEnRadianes = float(input("Ingrese el valor del ángulo en radianes: "))

angulo_sexagesimal = anguloEnRadianes * 180 / 3.14
angulo_centesimal = anguloEnRadianes * 200 / 3.14

print(f"El ángulo de {anguloEnRadianes} radianes es equivalente a:")
print(f"{angulo_sexagesimal:.2f} grados sexagesimales.")
print(f"{angulo_centesimal:.2f} grados centesimales.")

#-------------------------------------------------------------------------------

x1 = float(input("Ingrese la coordenada x: "))
y1 = float(input("Ingrese la coordenada y: "))
z1 = float(input("Ingrese la coordenada z: "))
x2 = float(input("Ingrese la coordenada x: "))
y2 = float(input("Ingrese la coordenada y: "))
z2 = float(input("Ingrese la coordenada z: "))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

print(f"La distancia entre los puntos ({x1}, {y1}, {z1}) y ({x2}, {y2}, {z2}) es: {distancia}")

#-----------------------------------------------------------------------------------

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su estatura: "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc:.2f}")

#__________________________________________________________________

